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
- Test App here - 
- [https://aicriticalminutes-zgkaue3f9cqg4ugprgvm6q.streamlit.app/](https://aicriticalminutes-zgkaue3f9cqg4ugprgvm6q.streamlit.app/)

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
## 📂 Project Structure
```
AI_Critical_Minutes/
│
├── data/
│ └── golden_ai_emergency_dataset.csv            # Synthetic emergency dataset
│
├── models/
│ └── emergency_risk_model.joblib                # Trained Random Forest model
│
├── pycache/                                     # Python cache files
│
├── ai_decision_engine.py                        # Converts risk level into Do / Don’t guidance
├── app.py                                       # FastAPI backend (prediction API)
├── eda_check.py                                 # EDA, correlation & data validation
├── generate_dataset.py                          # Synthetic dataset generation logic
├── inference_pipeline.py                        # End-to-end inference pipeline
├── train_model.py                               # Model training & evaluation
├── streamlit_app.py                             # Streamlit frontend with voice alerts
│
├── requirements.txt                             # Project dependencies
├── .gitignore                                   # Ignored files & folders
└── README.md                                    # Project documentation

```
---
##  Model Overview

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
```
User / Sensor Inputs
↓
Machine Learning Model
↓
Emergency Risk Level (0 / 1 / 2)
↓
AI Decision Engine
↓
Do / Don’t Guidance + Voice Alerts
```
---

## 🚀 API Usage

**Endpoint**
POST /predict


**Sample Response**
```json
{
  "predicted_risk_level": 2,
  "guidance": {
    "risk": "High Emergency",
    "message": "Critical condition detected. Immediate action required.",
    "dos": ["Lie down immediately", "Call emergency services"],
    "donts": ["Delay seeking help"],
    "alert": "HIGH"
  }
}
```
---

## Streamlit App

- Clean input form for vital signs
- Color-coded emergency alerts
- Voice guidance using browser’s native Text-to-Speech
- Designed to simulate real emergency decision    support

---

## Deployment & Tech Stack

- Backend: FastAPI (Render)
- Frontend: Streamlit
- ML: Python, Pandas, NumPy, Scikit-learn
- Model Storage: Joblib
--- 

### Navigate to:
- Swagger Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Root: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- Render: [https://ai-critical-minutes-2.onrender.com](https://ai-critical-minutes-2.onrender.com)
