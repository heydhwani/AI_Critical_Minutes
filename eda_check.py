import pandas as pd
import matplotlib.pyplot as plt


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