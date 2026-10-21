import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

model = joblib.load("regression.joblib")


class House(BaseModel):
    size: float
    nb_rooms: int
    garden: int


@app.get("/predict")
def predict_get():
    return {"y_pred": 2}


@app.post("/predict")
def predict_post(house: House):
    X = pd.DataFrame(
        [[house.size, house.nb_rooms, house.garden]],
        columns=["size", "nb_rooms", "garden"],
    )
    y_pred = model.predict(X)
    return {"y_pred": float(y_pred[0])}