import random
import pandas as pd
import numpy as np

NUM_ROWS = 5000
data = []


def detect_patterns(row):
    patterns = []

    if row["spo2"] < 90 or row["respiration_rate"] > 30:
        patterns.append("RESP")

    if row["heart_rate"] > 130 or row["systolic_bp"] > 180:
        patterns.append("CARDIO")

    if row["blood_sugar"] < 60 or row["blood_sugar"] > 300:
        patterns.append("GLUCO")

    if row["body_temp"] > 39.0 or row["body_temp"] < 35.0:
        patterns.append("TEMP")

    if (
        (row["heart_rate"] > 105 and row["spo2"] < 94) or
        (row["blood_sugar"] < 70 and row["heart_rate"] > 100)
    ):
        patterns.append("NEURO")

    return list(set(patterns))


def assign_risk(patterns, row):
    if (
        row["spo2"] < 85 or
        row["blood_sugar"] < 50 or
        row["heart_rate"] > 150
    ):
        return 2

    if len(patterns) >= 2:
        return 2

    if len(patterns) == 1:
        return 1

    return 0


for _ in range(NUM_ROWS):
    age = random.randint(18, 85)
    gender = random.choice(["Male", "Female"])
    heart_rate = random.randint(40, 160)
    systolic_bp = random.randint(90, 200)
    diastolic_bp = random.randint(60, 120)
    spo2 = random.randint(75, 100)
    respiration_rate = random.randint(8, 40)
    body_temp = round(random.uniform(34.0, 41.0), 1)
    blood_sugar = random.randint(40, 350)

    # ✅ FIRST: create row
    row = {
        "age": age,
        "gender": gender,
        "heart_rate": heart_rate,
        "systolic_bp": systolic_bp,
        "diastolic_bp": diastolic_bp,
        "spo2": spo2,
        "respiration_rate": respiration_rate,
        "body_temp": body_temp,
        "blood_sugar": blood_sugar
    }

    # ✅ THEN: AI thinks on row
    patterns = detect_patterns(row)
    risk_level = assign_risk(patterns, row)

    row["patterns"] = ",".join(patterns) if patterns else "NONE"
    row["emergency_risk_level"] = risk_level

    data.append(row)

print(data[0])

df = pd.DataFrame(data)

df.to_csv(
    "data/golden_ai_emergency_dataset.csv",
    index=False
)

print("Dataset saved successfully!")

