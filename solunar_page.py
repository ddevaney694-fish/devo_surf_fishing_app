import streamlit as st
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

def render():
    st.markdown("<h1 style='color:#58a6ff;'>Solunar Forecast</h1>", unsafe_allow_html=True)
    st.markdown("<div class='wave-divider'></div>", unsafe_allow_html=True)

    # Get real solunar data
    data = get_solunar_data()

    col1, col2, col3 = st.columns(3)
    with col1:
        storm_card("Moon Phase", data["moon_phase"])
    with col2:
        storm_card("Major Bite Window", data["major_window"])
    with col3:
        storm_card("Minor Bite Window", data["minor_window"])

    st.markdown("<div class='wave-divider'></div>", unsafe_allow_html=True)

    storm_card("Bite Rating", data["bite_rating"])

    st.markdown("<div class='wave-divider'></div>", unsafe_allow_html=True)

    st.info("Solunar engine is now active and generating live bite windows and moon phase data.")
