import streamlit as st
from pages.home import show_home
st.set_page_config(page_title="Hospital Readmission Prediction",page_icon="🏥",layout="wide")
show_home()
