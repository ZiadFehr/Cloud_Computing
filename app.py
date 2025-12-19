from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np

app = FastAPI(title= "Hospital Waiting Time Predictor")

# Load model once at startup
model = joblib.load("hospital_waiting_model.pkl")

class PredictionInput(BaseModel):
    doctor_type: str
    financial_class: str
    patient_type: str
    medication_revenue: float
    lab_cost: float
    consultation_revenue: float
    entry_hour: int
    entry_dayofweek: int
    entry_minute: int
    year: int
    month: int
    dayofweek: int

@app.get("/healthz")
def health_check():
    return{"status": "ok"}

@app.post("/predict")
def predict(input: PredictionInput):
    data = pd.DataFrame([input.model_dump()])
    log_prediction = model.predict(data)
    prediction = np.expm1(log_prediction)[0]

    return {
        "waiting_time_minutes": round(float(prediction), 2)
    }