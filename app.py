import streamlit as st
from datetime import datetime
import tides_page

# Load Storm Surf theme
with open("storm_surf_theme.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(
    page_title="Devo’s Surf Fishing – Dog Beach",
    layout="wide",
)

# Navigation
pages = {
    "Overview": "overview",
    "Solunar": "solunar",
  "Tides": "tides",  
}

st.sidebar.title("Devo’s Surf Fishing – Dog Beach")
choice = st.sidebar.radio("Navigate", list(pages.keys()))

# Page loader
if choice == "Overview":
    import overview_page as page
elif choice == "Solunar":
    import solunar_page as page
 elif choice == "Tides":
    import tides_page as page   

page.render()
