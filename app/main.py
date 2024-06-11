from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List
from .model import IrisModel
import os

app = FastAPI()

model = IrisModel()
model_path = os.path.join(os.path.dirname(__file__), 'xgb_iris_model.pkl')
model.load_model(model_path)

class IrisRequest(BaseModel):
    data: List[List[float]] = Field(..., min_items=1)

@app.post("/predict")
def predict(request: IrisRequest):
    for item in request.data:
        if len(item) != 4:
            raise HTTPException(status_code=400, detail="Each item in the data list must have exactly 4 float values.")
    try:
        prediction = model.predict(request.data)
        return {"prediction": prediction.tolist()}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.exception_handler(Exception)
def validation_exception_handler(request, err):
    return HTTPException(status_code=400, detail=str(err))


