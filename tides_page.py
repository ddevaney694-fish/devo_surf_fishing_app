import streamlit as st
import matplotlib.pyplot as plt
from tide_tools import get_tide_summary

def render():
    st.markdown("<h1 style='color:#58a6ff;'>Tide Chart – Morro Bay</h1>", unsafe_allow_html=True)
    st.markdown("<div class='wave-divider'></div>", unsafe_allow_html=True)

    tide = get_tide_summary()

    # If no tide data, show fallback message
    if not tide["points"]:
        st.error("No tide data available from NOAA at the moment.")
        return

    points = tide["points"]
    current_height = tide["current_height"]
    current_stage = tide["current_stage"]

    # Build chart data
    times = [p["time"] for p in points]
    heights = [p["height_ft"] for p in points]

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(times, heights, color="#58a6ff", linewidth=2)
    ax.set_title("Today's Tide Chart – Morro Bay")
    ax.set_ylabel("Height (ft)")
    ax.grid(True, alpha=0.3)

    # Mark current tide height
    if current_height is not None:
        ax.axhline(current_height, color="orange", linestyle="--", linewidth=1)

    st.pyplot(fig)

    # Display summary
    st.markdown(f"### Current Tide Height: **{current_height} ft**")
    st.markdown(f"### Tide Stage: **{current_stage}**")
