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

    # Top row: Moon + Major + Minor
    col1, col2, col3 = st.columns(3)
    with col1:
        storm_card("Moon Phase", data["moon_phase"])
    with col2:
        storm_card("Major Bite Window", data["major_window"])
    with col3:
        storm_card("Minor Bite Window", data["minor_window"])

    st.markdown("<div class='wave-divider'></div>", unsafe_allow_html=True)

    # Middle row: Sunrise + Sunset + Tide Stage
    col4, col5, col6 = st.columns(3)
    with col4:
        storm_card("Sunrise", data["sunrise"])
    with col5:
        storm_card("Sunset", data["sunset"])
    with col6:
        storm_card("Tide Stage", data["tide_stage"])

    st.markdown("<div class='wave-divider'></div>", unsafe_allow_html=True)

    # Bottom row: Bite Rating + Solunar Score + Bite Counts
    col7, col8, col9 = st.columns(3)
    with col7:
        storm_card("Bite Rating", data["bite_rating"])
    with col8:
        storm_card("Solunar Score", data["solunar_score"])
    with col9:
        storm_card("Bite Windows", f"{data['major_count']} Major / {data['minor_count']} Minor")

    st.markdown("<div class='wave-divider'></div>", unsafe_allow_html=True)

    st.info("Solunar engine is now fully active with moon phase, bite windows, tide stage, sunrise/sunset, and solunar scoring.")
