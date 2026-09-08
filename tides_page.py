import streamlit as st
import matplotlib.pyplot as plt
from tide_tools import get_tide_summary

def render():
    st.markdown("<h1 style='color:#58a6ff;'>Tide Chart – Morro Bay</h1>", unsafe_allow_html=True)
    st.markdown("<div class='wave-divider'></div>", unsafe_allow_html=True)

    tide = get_tide_summary()

    points = tide["points"]
    current_height = tide["current_height"]
    current_stage = tide["current_stage"]

    if not points:
        st.error("No tide data available.")
        return

    # Extract data for plotting
    times = [p["time"] for p in points]
    heights = [p["height_ft"] for p in points]

    # Build the chart
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(times, heights, color="#58a6ff", linewidth=2)

    ax.set_title("Today's Tide Curve – Morro Bay", fontsize=14)
    ax.set_ylabel("Tide Height (ft)")
    ax.set_xlabel("Time")

    # Mark current tide height
    ax.axhline(current_height, color="orange", linestyle="--", linewidth=1)
    ax.text(times[len(times)//2], current_height + 0.1,
            f"Current: {current_height:.1f} ft ({current_stage})",
            color="orange")

    plt.xticks(rotation=45)
    plt.tight_layout()

    st.pyplot(fig)

    st.markdown("<div class='wave-divider'></div>", unsafe_allow_html=True)

    # Summary cards
    st.markdown("<h3 style='color:#58a6ff;'>Current Tide Status</h3>", unsafe_allow_html=True)
    st.write(f"**Current Tide Height:** {current_height:.1f} ft")
    st.write(f"**Tide Stage:** {current_stage}")
