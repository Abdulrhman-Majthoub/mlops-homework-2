from fastapi import FastAPI
from pydantic import BaseModel

from src.feature_engineering import hash_bucket


app = FastAPI()


class InputData(BaseModel):
    feature: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict(data: InputData):
    bucket = hash_bucket(data.feature, num_buckets=1000)
    prediction = bucket / 1000.0  # dummy numeric prediction
    return {"prediction": prediction}
