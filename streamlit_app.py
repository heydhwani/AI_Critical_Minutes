import streamlit as st
import streamlit.components.v1 as components
import requests


# -----------------------
# Page config
# -----------------------
st.set_page_config(
    page_title="AI Critical Minutes",
    page_icon="🚨",
    layout="centered"
)


# -----------------------
# Title
# -----------------------
st.title("🚨 AI Critical Minutes")
st.write(
    "This system analyzes vital signs and provides **real-time emergency guidance** "
    "during critical minutes."
)

st.divider()


# -----------------------
# Input section
# -----------------------
st.subheader("🩺 Enter Patient Vitals")

age = st.number_i_
