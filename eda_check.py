import pandas as pd


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
