from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import numpy as np
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
    if prob < 0.33:
        return "Low"
    elif prob < 0.66:
        return "Medium"
    return "High"

def get_suggestion(prob):
    if prob < 0.33:
        return "Keep up the good work!"
    elif prob < 0.66:
        return "Provide more support and engagement."
    return "Urgent action needed: Assign mentoring or career development."

# Pydantic model for input
class ChurnInput(BaseModel):
    Target: float
    Satisfaction: float
    Manager: float
    Hours: float
    Distance: float

@app.post("/predict")
async def predict(data: ChurnInput):
    # Convert input to model format
    input_data = np.array([[data.Target, data.Satisfaction, data.Manager, data.Hours, data.Distance]])
    input_scaled = scaler.transform(input_data)

    # Predict
    prob = model.predict_proba(input_scaled)[0][1]
    risk = get_risk_group(prob)
    suggestion = get_suggestion(prob)

    # Save to history
    history_data.append({
        "features": data.dict(),
        "probability": float(round(prob, 4)),
        "risk": risk,
        "suggestion": suggestion
    })

    return JSONResponse(content={
        "probability": round(prob, 4),
        "risk": risk,
        "suggestion": suggestion
    })
