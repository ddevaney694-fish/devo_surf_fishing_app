import streamlit as st
from tide_tools import get_tide_series

def render():
    st.markdown("<h1 style='color:#58a6ff;'>Tide Conditions</h1>", unsafe_allow_html=True)

    # Get tide data
    df = get_tide_series()
    current_height = df["height_ft"].iloc[0]

    # Current tide height
    st.subheader("Current Tide Height")
    st.metric(label="Height", value=f"{current_height:.1f} ft")

    # Tide graph
    st.subheader("Tide Graph")
    st.line_chart(df.set_index("time")["height_ft"])