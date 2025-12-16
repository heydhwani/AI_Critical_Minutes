from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import os

from ai_decision_engine import get_emergency_guidance


# App init

app = FastAPI(title="AI Critical Minutes API")

# Load model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "models", "emergency_risk_model.joblib")
model = joblib.load(MODEL_PATH)



# Input schema

class VitalsInput(BaseModel):
    age: int
    heart_rate: int
    systolic_bp: int
    diastolic_bp: int
    spo2: int
    respiration_rate: int
    body_temp: float
    blood_sugar: int

@app.get("/")
def home():
    return {"message": "AI Critical Minutes API is running"}


# Prediction endpoint

@app.post("/predict")
def predict_emergency(vitals: VitalsInput):
    # Convert input to DataFrame
    input_df = pd.DataFrame([vitals.dict()])

    # Predict risk
    risk_level = int(model.predict(input_df)[0])

    # AI guidance
    guidance = get_emergency_guidance(risk_level)

    return {
        "predicted_risk_level": risk_level,
        "guidance": guidance
    }
