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
    st.markdown("<h1 style='color:#58a6ff;'>Species Bite Forecast</h1>", unsafe_allow_html=True)
    st.markdown("<div class='wave-divider'></div>", unsafe_allow_html=True)

    # Placeholder values (real species engine coming later)
    halibut_window = "11:00 AM – 12:30 PM"
    halibut_rating = "GOOD"

    perch_window = "6:00 AM – 8:00 AM"
    perch_rating = "FAIR"

    striper_window = "5:30 PM – 7:00 PM"
    striper_rating = "GOOD"

    # --- Halibut ---
    st.markdown("<h3 style='color:#58a6ff;'>Halibut</h3>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        storm_card("Bite Window", halibut_window)
    with col2:
        storm_card("Rating", halibut_rating)

    st.markdown("<div class='wave-divider'></div>", unsafe_allow_html=True)

    # --- Perch ---
    st.markdown("<h3 style='color:#58a6ff;'>Perch</h3>", unsafe_allow_html=True)
    col3, col4 = st.columns(2)
    with col3:
        storm_card("Bite Window", perch_window)
    with col4:
        storm_card("Rating", perch_rating)

    st.markdown("<div class='wave-divider'></div>", unsafe_allow_html=True)

    # --- Striper ---
    st.markdown("<h3 style='color:#58a6ff;'>Striper</h3>", unsafe_allow_html=True)
    col5, col6 = st.columns(2)
    with col5:
        storm_card("Bite Window", striper_window)
    with col6:
        storm_card("Rating", striper_rating)

    st.markdown("<div class='wave-divider'></div>", unsafe_allow_html=True)

    st.info("Species engine will be connected soon for live bite windows and ratings.")