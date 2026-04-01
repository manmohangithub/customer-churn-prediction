from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Churn Prediction API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = pickle.load(open("model.pkl","rb"))
encoders = pickle.load(open("encoders.pkl","rb"))
features = pickle.load(open("features.pkl","rb"))

# ✅ FIXED MODEL SCHEMA
class CustomerData(BaseModel):
    TenureMonths: int
    MonthlyCharges: float
    TotalCharges: float
    Contract: str
    InternetService: str
    PaymentMethod: str
    OnlineSecurity: str
    TechSupport: str

@app.get("/")
def home():
    return {"status":"running"}

@app.post("/predict")
def predict(data: CustomerData):
    data = data.dict()

    processed = []

    for f in features:
        val = data.get(f)

        if f in encoders:
            val = encoders[f].transform([val])[0]

        processed.append(val)

    arr = np.array(processed).reshape(1,-1)

    pred = model.predict(arr)[0]
    prob = model.predict_proba(arr)[0][1]

    return {"churn": int(pred), "probability": float(prob)}

@app.get("/feature-importance")
def importance():
    return dict(zip(features, model.feature_importances_.tolist()))