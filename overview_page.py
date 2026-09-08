import streamlit as st
from datetime import datetime
from solunar_tools import get_solunar_data
from surf_tools import get_surf_conditions

def storm_card(title, value):
    st.markdown(
        f"""
        <div class="storm-card">
            <div class="storm-title">{title}</div>
            <div class="storm-value">{value}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def storm_badge(label, badge_type):
    css_class = {
        "GO": "storm-badge-go",
        "CAUTION": "storm-badge-caution",
        "NO-GO": "storm-badge-nogo",
    }.get(badge_type, "storm-badge-caution")

    st.markdown(
        f"""
        <div class="{css_class}">
            {label}
        </div>
        """,
        unsafe_allow_html=True,
    )

def render():
    st.markdown("<h1 style='color:#58a6ff;'>Devo’s Surf Fishing – Dog Beach</h1>", unsafe_allow_html=True)
    st.markdown("<div class='wave-divider'></div>", unsafe_allow_html=True)

    # --- Overview Header ---
    st.markdown("<h2 style='color:#58a6ff;'>Storm Surf Overview</h2>", unsafe_allow_html=True)

    # --- Current Time ---
    import pytz
    pst = pytz.timezone("America/Los_Angeles")
    now = datetime.now(pst).strftime("%A, %B %d • %I:%M %p")
    storm_card("Current Time", now)
    st.markdown("<div class='wave-divider'></div>", unsafe_allow_html=True)

    # --- Get real engines ---
    solunar = get_solunar_data()
    surf = get_surf_conditions()

    # --- Buoy Info ---
    st.markdown("<h3 style='color:#58a6ff;'>Buoy Source</h3>", unsafe_allow_html=True)
    storm_card("Buoy Used", surf["buoy_source"])
    storm_card("Buoy Timestamp", surf["buoy_time"])
    st.markdown("<div class='wave-divider'></div>", unsafe_allow_html=True)

    # --- Surf conditions ---
    col1, col2, col3 = st.columns(3)
    with col1:
        storm_card("Breakers", surf["breakers"])
    with col2:
        storm_card("Wave Sets", surf["sets"])
    with col3:
        storm_card("Surf Temp", surf["surf_temp"])

    col4, col5, col6 = st.columns(3)
    with col4:
        storm_card("Surf Energy", surf["surf_energy"])
    with col5:
        storm_card("Tide Stage", solunar["tide_stage"])
    with col6:
        storm_card("Solunar Score", solunar["solunar_score"])

    st.markdown("<div class='wave-divider'></div>", unsafe_allow_html=True)

    # --- Bite windows ---
    col7, col8 = st.columns(2)
    with col7:
        storm_card("Major Bite Window", solunar["major_window"])
    with col8:
        storm_card("Minor Bite Window", solunar["minor_window"])

    st.markdown("<div class='wave-divider'></div>", unsafe_allow_html=True)

    # --- Fishing status ---
    st.markdown("<h3 style='color:#58a6ff;'>Fishing Status</h3>", unsafe_allow_html=True)

    combined_score = int((surf["fishability_score"] + solunar["solunar_score"]) / 2)

    if combined_score >= 70:
        go_status = "GO"
    elif combined_score >= 50:
        go_status = "CAUTION"
    else:
        go_status = "NO-GO"

    storm_badge(f"{go_status} • {combined_score}", go_status)
