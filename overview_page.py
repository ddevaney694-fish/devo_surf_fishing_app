import streamlit as st
from datetime import datetime
from solunar_tools import get_solunar_data

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

    # --- Get real solunar data ---
    data = get_solunar_data()

    # --- Surf placeholders (we will replace these later with real NOAA data) ---
    breakers = "2.5 ft"
    energy = "112 kJ"
    surf_temp = "57°F"

    # --- Card Grid Layout ---
    col1, col2, col3 = st.columns(3)
    with col1:
        storm_card("Breakers", breakers)
    with col2:
        storm_card("Energy", energy)
    with col3:
        storm_card("Surf Temp", surf_temp)

    col4, col5, col6 = st.columns(3)
    with col4:
        storm_card("Tide Stage", data["tide_stage"])
    with col5:
        storm_card("Moon Phase", data["moon_phase"])
    with col6:
        storm_card("Solunar Score", data["solunar_score"])

    st.markdown("<div class='wave-divider'></div>", unsafe_allow_html=True)

    # --- Bite Windows ---
    col7, col8 = st.columns(2)
    with col7:
        storm_card("Major Bite Window", data["major_window"])
    with col8:
        storm_card("Minor Bite Window", data["minor_window"])

    st.markdown("<div class='wave-divider'></div>", unsafe_allow_html=True)

    # --- GO / NO-GO Badge ---
    st.markdown("<h3 style='color:#58a6ff;'>Fishing Status</h3>", unsafe_allow_html=True)

    # Simple logic for now — we will improve this later
    go_status = "GO" if data["solunar_score"] >= 60 else "CAUTION"
    storm_badge(go_status, go_status)
