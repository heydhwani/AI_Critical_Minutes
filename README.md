# 🚨 AI Critical Minutes – Emergency Risk Detection System

AI Critical Minutes is an **AI-powered emergency risk detection and decision-support system** designed for the **golden critical minutes** of a medical emergency.  
Instead of predicting diseases, the system focuses on detecting **physiological instability** using vital signs and provides **clear Do’s & Don’ts with voice alerts** in real time.

---

## 🚀 Key Features

- Detects **Emergency Risk Level**: Normal / Warning / High Emergency
- Uses **multiple vital signs together** (not single-parameter thresholds)
- **Random Forest–based supervised multi-class classification**
- AI decision engine that converts predictions into **actionable guidance**
- **Repeated voice alerts** for critical emergencies to ensure attention
- Interactive **Streamlit UI** with color-coded alerts
- **FastAPI backend** deployed on Render
- JSON-based API tested using Postman
- End-to-end system: dataset → model → API → UI → voice alerts

---

## 🧪 Dataset Description

- **Type**: Custom synthetic emergency dataset
- **Samples**: ~5,000
- **Target**: `emergency_risk_level`  
  - 0 → Normal  
  - 1 → Warning  
  - 2 → High Emergency
- **Features**:
  - Age
  - Heart Rate
  - Systolic & Diastolic BP
  - SpO₂
  - Respiration Rate
  - Body Temperature
  - Blood Sugar

Dataset was designed using **realistic medical ranges** and weighted sampling to simulate both normal and critical conditions.

---

## 🧠 Model Overview

- **Problem Type**: Supervised Multi-Class Classification
- **Algorithm**: Random Forest Classifier
- **Design Focus**:
  - High recall for **High Emergency** cases
  - Safety-first prediction strategy
  - Multi-signal pattern detection
- **Objective**: Assist decision-making during critical minutes (not diagnosis)

---

## 📈 Model Performance

- **Accuracy**: ~97%
- **Recall (High Emergency)**: Prioritized to avoid missed critical cases
- **Confusion Matrix**:  
  - Very low false negatives for emergency class  
  - Acceptable overlap between Normal and Warning cases

> In emergency systems, **recall is more important than raw accuracy**.

---

## 📊 EDA & Correlation Insights

- Verified class distribution and data validity
- No missing or duplicate records
- Correlation analysis showed:
  - Strong influence of **SpO₂, heart rate, respiration rate**
  - Extreme temperature and blood sugar values linked to emergencies

EDA insights were used to support both model training and decision logic.

---

## 🏗️ System Architecture

User / Sensor Inputs
↓
Machine Learning Model
↓
Emergency Risk Level (0 / 1 / 2)
↓
AI Decision Engine
↓
Do / Don’t Guidance + Voice Alerts
