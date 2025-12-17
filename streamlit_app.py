import streamlit as st
import streamlit.components.v1 as components

import requests


# Page config

st.set_page_config(
    page_title="AI Critical Minutes",
    page_icon="🚨",
    layout="centered"
)


# Title

st.title("🚨 AI Critical Minutes")
st.write(
    "This system analyzes vital signs and provides **real-time emergency guidance** "
    "during critical minutes."
)

st.divider()


# Input section

st.subheader("🩺 Enter Patient Vitals")

age = st.number_input("Age", min_value=1, max_value=120, value=30)

heart_rate = st.number_input("Heart Rate (bpm)", min_value=30, max_value=200, value=75)
systolic_bp = st.number_input("Systolic BP (mmHg)", min_value=80, max_value=250, value=120)
diastolic_bp = st.number_input("Diastolic BP (mmHg)", min_value=40, max_value=150, value=80)

spo2 = st.number_input("SpO₂ (%)", min_value=50, max_value=100, value=98)
respiration_rate = st.number_input("Respiration Rate (per min)", min_value=8, max_value=60, value=16)

body_temp = st.number_input("Body Temperature (°C)", min_value=34.0, max_value=42.0, value=36.8)
blood_sugar = st.number_input("Blood Sugar (mg/dL)", min_value=40, max_value=400, value=100)

st.divider()


# API URL (Render)

API_URL = "https://ai-critical-minutes-2.onrender.com/predict"



def speak_list(title, items):
    text = title + ". " + ". ".join(items)
    html_code = f"""
    <script>
    var msg = new SpeechSynthesisUtterance("{text}");
    msg.volume = 1.0;
    msg.rate = 0.95;
    msg.pitch = 1.0;
    window.speechSynthesis.speak(msg);
    </script>
    """
    components.html(html_code)


# Button

if st.button("🔍 Check Emergency Risk"):
    payload = {
        "age": age,
        "heart_rate": heart_rate,
        "systolic_bp": systolic_bp,
        "diastolic_bp": diastolic_bp,
        "spo2": spo2,
        "respiration_rate": respiration_rate,
        "body_temp": body_temp,
        "blood_sugar": blood_sugar
    }

    try:
        response = requests.post(API_URL, json=payload, timeout=10)

        if response.status_code == 200:
            result = response.json()
            guidance = result["guidance"]

            st.divider()

            
            # Alert styling
            
            if guidance["alert"] == "HIGH":
                st.error("🚨 HIGH EMERGENCY")

                speak_list(
                    "Critical condition detected. Follow these steps",
                     guidance["dos"][:3]   # sirf top 3 DOs
                )

                speak_list(
                    "Do not do the following",
                     guidance["donts"][:2] # sirf top 2 DON’Ts
                )

            st.write(f"**{guidance['message']}**")

            
            # Dos & Don'ts
            
            col1, col2 = st.columns(2)

            with col1:
                st.subheader("✅ Do")
                for d in guidance["dos"]:
                    st.write("•", d)

            with col2:
                st.subheader("❌ Don't")
                for d in guidance["donts"]:
                    st.write("•", d)

        else:
            st.error("API error. Please try again.")

    except Exception as e:
        st.error("Unable to connect to backend service.")
