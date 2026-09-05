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

def render():
    st.markdown("<h1 style='color:#58a6ff;'>Solunar Forecast</h1>", unsafe_allow_html=True)
    st.markdown("<div class='wave-divider'></div>", unsafe_allow_html=True)

    # Placeholder values (real solunar engine coming later)
    moon_phase = "Waning Gibbous"
    major_window = "10:45 AM – 12:15 PM"
    minor_window = "5:20 PM – 6:05 PM"
    bite_rating = "GOOD"

    col1, col2, col3 = st.columns(3)
    with col1:
        storm_card("Moon Phase", moon_phase)
    with col2:
        storm_card("Major Bite Window", major_window)
    with col3:
        storm_card("Minor Bite Window", minor_window)

    st.markdown("<div class='wave-divider'></div>", unsafe_allow_html=True)

    storm_card("Bite Rating", bite_rating)

    st.markdown("<div class='wave-divider'></div>", unsafe_allow_html=True)

    st.info("Solunar engine will be connected soon for live bite windows and moon phase data.")