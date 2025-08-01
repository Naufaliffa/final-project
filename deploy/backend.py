from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import numpy as np
import pandas as pd
import pickle
import os
from fastapi.staticfiles import StaticFiles

# Load model and scaler
model = pickle.load(open("model/model.pkl", "rb"))
scaler = pickle.load(open("model/scaler.pkl", "rb"))

# FastAPI app
app = FastAPI()

if not os.path.exists("static"):
    os.makedirs("static")
app.mount("/static", StaticFiles(directory="static"), name="static")

# In-memory history
history_data = []

# Risk group mapping
def get_risk_group(prob):
    if prob < 0.38:
        return "Low"
    elif prob < 0.69:
        return "Medium"
    return "High"

def get_suggestion(prob):
    if prob < 0.38:
        return "Keep up the good work!"
    elif prob < 0.69:
        return "Provide more support and engagement."
    return "Urgent action needed: Assign mentoring or career development."

# Pydantic model for input
class ChurnInput(BaseModel):
    Target: float
    Hours: float
    Satisfaction: float
    Manager: float
    Tenure: float
    Distance: float
    Age: float
    Salary: float
    Experience: float
    Marital: int


@app.post("/predict")
async def predict(data: ChurnInput):
    try:
        # Reconstruct input with all features (including engineered)
        df = pd.DataFrame([{
            "target_achievement": data.Target,
            "working_hours_per_week": data.Hours,
            "job_satisfaction": data.Satisfaction,
            "manager_support_score": data.Manager,
            "company_tenure_years": data.Tenure,
            "distance_to_office_km": data.Distance,
            "tenure_per_age": data.Age,
            "income_per_hour": data.Salary,
            "experience_to_tenure": data.Experience,
            "marital_status_Single": data.Marital,
        }])

        # Create engineered features
        # df['tenure_per_age'] = df['company_tenure_years'] / (df['age'].replace(0, np.nan))                        # Indikasi loyalitas (makin tinggi makin loyal)
        # df['income_per_hour'] = df['salary'] / ((df['working_hours_per_week'].replace(0, np.nan)) * 4.3)        # Representasi efisiensi gaji (gaji kecil bisa saja peluang jadi churn)
        # df['experience_to_tenure'] = df['experience_years'] / (df['company_tenure_years'] + 1)

        # Final selected features
        selected_features = [
            "target_achievement",
            "working_hours_per_week",
            "job_satisfaction",
            "manager_support_score",
            "company_tenure_years",
            "distance_to_office_km",
            "tenure_per_age",
            "income_per_hour",
            "experience_to_tenure",
            "marital_status_Single",
        ]

        X = df[selected_features]
        X_scaled = scaler.transform(X)

        prob = float(model.predict_proba(X_scaled)[0][1])
        risk = get_risk_group(prob)
        
        suggestion = get_suggestion(prob)

        # Save to session history (in-memory only)
        history_data.append({
            "features": data.dict(),
            "probability": round(prob, 4),
            "risk": risk,
            "suggestion": suggestion
        })

        return JSONResponse(content={
            "probability": round(prob, 4),
            "risk": risk,
            "suggestion": suggestion
        })
    
    except Exception as e:
        import traceback
        print("❌ Backend error:\n", traceback.format_exc())
        return JSONResponse(content={"error": f"Prediction failed: {e}"}, status_code=500)
