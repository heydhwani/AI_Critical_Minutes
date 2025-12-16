import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import joblib
import os

# Load dataset
df = pd.read_csv("data/golden_ai_emergency_dataset.csv")

# Features & target
X = df[
    [
        "age",
        "heart_rate",
        "systolic_bp",
        "diastolic_bp",
        "spo2",
        "respiration_rate",
        "body_temp",
        "blood_sugar"
    ]
]

y = df["emergency_risk_level"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Random Forest Model

model = RandomForestClassifier(
    n_estimators=200,
    max_depth=10,
    class_weight="balanced",
    random_state=42
)

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Evaluation
print("\nCONFUSION MATRIX:")
print(confusion_matrix(y_test, y_pred))

print("\nCLASSIFICATION REPORT:")
print(classification_report(y_test, y_pred))


# Create models directory if not exists
os.makedirs("models", exist_ok=True)

# Save trained model
joblib.dump(model, "models/emergency_risk_model.joblib")

print("Model saved at models/emergency_risk_model.joblib")