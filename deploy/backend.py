from fastapi import FastAPI, Request, File, UploadFile
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import numpy as np
import pandas as pd
import pickle
import os
from io import StringIO
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
    Satisfaction: float
    Manager: float
    Distance: float
    Marital: int
    Hours: float
    Tenure: float
    Commission: float
    Age: float

@app.post("/predict")
async def predict(data: ChurnInput):
    try:
        # Reconstruct input with all features (including engineered)
        df = pd.DataFrame([{
            "target_achievement": data.Target,
            "job_satisfaction": data.Satisfaction,
            "manager_support_score": data.Manager,
            "distance_to_office_km": data.Distance,
            "marital_status_Single": data.Marital,
            "working_hours_per_week": data.Hours,
            "company_tenure_years": data.Tenure,
            "commission_rate": data.Commission,
            "overtime_hours_per_week": data.Hours,
            "age": data.Age
        }])

        # Create engineered features
        df["overwork_ratio"] = df["overtime_hours_per_week"] / df["working_hours_per_week"].replace(0, np.nan)
        df["tenure_per_age"] = df["company_tenure_years"] / df["age"].replace(0, np.nan)

        # Final selected features
        selected_features = [
            "target_achievement",
            "job_satisfaction",
            "manager_support_score",
            "distance_to_office_km",
            "marital_status_Single",
            "working_hours_per_week",
            "company_tenure_years",
            "tenure_per_age",
            "commission_rate",
            "overwork_ratio"
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

@app.post("/bulk_predict")
async def bulk_predict(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        df = pd.read_csv(StringIO(contents.decode("utf-8")))

        # Mapping raw input columns to required features
        feature_aliases = {
            "target_achievement": ["target", "target_achievement"],
            "job_satisfaction": ["satisfaction", "job_satisfaction"],
            "manager_support_score": ["manager", "manager_support_score"],
            "distance_to_office_km": ["distance", "distance_to_office_km"],
            "marital_status_Single": ["marital", "marital_status"],
            "working_hours_per_week": ["hours", "working_hours_per_week"],
            "company_tenure_years": ["tenure", "company_tenure_years"],
            "commission_rate": ["commission", "commission_rate"],
            "age": ["age"]
        }

        col_map = {}
        for key, aliases in feature_aliases.items():
            for alias in aliases:
                matches = [col for col in df.columns if alias.lower() in col.lower()]
                if matches:
                    col_map[key] = matches[0]
                    break

        print("📎 Column map:", col_map)

        missing_keys = [key for key in feature_aliases if key not in col_map]
        if missing_keys:
            return JSONResponse(
                content={"error": f"Missing required features in CSV: {missing_keys}"},
                status_code=400
            )

        # Rename columns accordingly
        df_intermediate = df[[col_map[k] for k in col_map]].copy()
        df_intermediate.columns = list(col_map.keys())
        df_clean = df_intermediate

        # Normalize target_achievement if needed
        if df_clean["target_achievement"].max() > 1:
            df_clean["target_achievement"] = df_clean["target_achievement"] / 100.0

        # Encode marital_status_Single (text to 1/0)
        df_clean["marital_status_Single"] = df_clean["marital_status_Single"].astype(str).str.lower().map({
            "single": 1, "married": 0, "1": 1, "0": 0
        }).fillna(0)

        # Feature engineering
        df_clean["overtime_hours_per_week"] = df_clean["working_hours_per_week"]
        df_clean["overwork_ratio"] = df_clean["overtime_hours_per_week"] / df_clean["working_hours_per_week"].replace(0, np.nan)
        df_clean["tenure_per_age"] = df_clean["company_tenure_years"] / df_clean["age"].replace(0, np.nan)

        # Final features
        selected_features = [
            "target_achievement", "job_satisfaction", "manager_support_score", "distance_to_office_km",
            "marital_status_Single", "working_hours_per_week", "company_tenure_years",
            "tenure_per_age", "commission_rate", "overwork_ratio"
        ]

        print("🔍 Final columns:", df_clean.columns.tolist())
        missing_final = [col for col in selected_features if col not in df_clean.columns]
        if missing_final:
            return JSONResponse(content={"error": f"Missing required engineered features: {missing_final}"}, status_code=400)

        X = df_clean[selected_features]
        X_scaled = scaler.transform(X)
        proba = model.predict_proba(X_scaled)[:, 1]

        batch_results = []
        for i, prob in enumerate(proba):
            risk = get_risk_group(prob)
            suggestion = get_suggestion(prob)

            record_features = df_clean.iloc[i][selected_features].to_dict()
            if "age" in df_clean.columns:
                record_features["age"] = df_clean.iloc[i]["age"]

            record = {
                "features": record_features,
                "probability": round(float(prob), 4),
                "risk": risk,
                "suggestion": suggestion
            }

            history_data.append(record)
            batch_results.append(record)

        return JSONResponse(content={"results": batch_results})

    except Exception as e:
        import traceback
        print("❌ Bulk prediction error:\n", traceback.format_exc())
        return JSONResponse(content={"error": f"Bulk prediction failed: {e}"}, status_code=500)
