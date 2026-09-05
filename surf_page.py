import streamlit as st

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
    st.markdown("<h1 style='color:#58a6ff;'>Surf Fishing Conditions</h1>", unsafe_allow_html=True)
    st.markdown("<div class='wave-divider'></div>", unsafe_allow_html=True)

    # Placeholder values (real engine coming later)
    breakers = "2.5 ft"
    energy = "112 kJ"
    surf_temp = "57°F"
    set_behavior = "Light 2–3 wave sets"
    fishability = "GOOD"
    go_status = "GO"

    col1, col2, col3 = st.columns(3)
    with col1:
        storm_card("Breakers", breakers)
    with col2:
        storm_card("Energy", energy)
    with col3:
        storm_card("Surf Temp", surf_temp)

    col4, col5 = st.columns(2)
    with col4:
        storm_card("Set Behavior", set_behavior)
    with col5:
        storm_card("Fishability", fishability)

    st.markdown("<div class='wave-divider'></div>", unsafe_allow_html=True)

    st.markdown("<h3 style='color:#58a6ff;'>Fishing Status</h3>", unsafe_allow_html=True)
    storm_badge(go_status, go_status)