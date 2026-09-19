from pydantic import BaseModel

class Prediction(BaseModel):
    label: str
    confidence: float

class PredictionResponse(BaseModel):
    predictions: list[Prediction]