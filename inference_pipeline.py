import joblib
import pandas as pd

from ai_decision_engine import get_emergency_guidance



# Load trained model

model = joblib.load("models/emergency_risk_model.joblib")


def predict_emergency(vitals: dict):
    """
    Takes raw vitals as input,
    predicts emergency risk,
    and returns AI guidance.
    """

    # Convert input dict to DataFrame
    input_df = pd.DataFrame([vitals])

    # Model prediction
    risk_level = int(model.predict(input_df)[0])

    # AI decision logic
    guidance = get_emergency_guidance(risk_level)

    # Combine output
    result = {
        "predicted_risk_level": risk_level,
        "guidance": guidance
    }

    return result



# Test the full pipeline

if __name__ == "__main__":
    sample_vitals = {
        "age": 55,
        "heart_rate": 145,
        "systolic_bp": 185,
        "diastolic_bp": 95,
        "spo2": 82,
        "respiration_rate": 34,
        "body_temp": 39.5,
        "blood_sugar": 110
    }

    output = predict_emergency(sample_vitals)

    print("\n=== FULL AI OUTPUT ===")
    print(output)



