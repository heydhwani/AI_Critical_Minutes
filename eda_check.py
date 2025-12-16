import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("data/golden_ai_emergency_dataset.csv")

print("====== BASIC INFO ======")
print("Shape:", df.shape)
print("\nData types:")
print(df.dtypes)

print("\n====== NULL CHECK ======")
print(df.isnull().sum())

print("\n====== DUPLICATE CHECK ======")
print("Duplicate rows:", df.duplicated().sum())

print("\n====== LABEL CHECK ======")
print("\nRisk levels:")
print(df["emergency_risk_level"].value_counts())

print("\nPatterns:")
print(df["patterns"].value_counts())

print("\n====== SAMPLE DATA ======")
print(df.head())

print("\n====== QUICK STATS ======")
print(df.describe())


# VISUAL EDA

df["emergency_risk_level"].value_counts().sort_index().plot(kind="bar")
plt.xlabel("Risk Level (0 = Normal, 1 = Warning, 2 = High)")
plt.ylabel("Count")
plt.title("Emergency Risk Level Distribution")
plt.tight_layout()
plt.show()

# Select only numeric columns for correlation
numeric_cols = [
    "heart_rate",
    "systolic_bp",
    "diastolic_bp",
    "spo2",
    "respiration_rate",
    "body_temp",
    "blood_sugar",
    "emergency_risk_level"
]

corr = df[numeric_cols].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap of Vitals and Emergency Risk Level")
plt.tight_layout()
plt.show()