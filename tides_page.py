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
    st.markdown("<h1 style='color:#58a6ff;'>Tide Conditions</h1>", unsafe_allow_html=True)
    st.markdown("<div class='wave-divider'></div>", unsafe_allow_html=True)

    # Placeholder values (real tide engine coming later)
    tide_stage = "Incoming"
    next_high = "4:12 PM • 5.1 ft"
    next_low = "10:38 PM • 0.7 ft"
    current_height = "3.4 ft"

    # --- Card Grid Layout ---
    col1, col2, col3 = st.columns(3)
    with col1:
        storm_card("Tide Stage", tide_stage)
    with col2:
        storm_card("Next High Tide", next_high)
    with col3:
        storm_card("Next Low Tide", next_low)

    st.markdown("<div class='wave-divider'></div>", unsafe_allow_html=True)

    storm_card("Current Tide Height", current_height)

    st.markdown("<div class='wave-divider'></div>", unsafe_allow_html=True)

    # Placeholder for tide graph (added later)
    st.markdown(
        "<h3 style='color:#58a6ff;'>Tide Graph</h3>",
        unsafe_allow_html=True
    )
    st.info("Tide graph will appear here once the tide engine is connected.")