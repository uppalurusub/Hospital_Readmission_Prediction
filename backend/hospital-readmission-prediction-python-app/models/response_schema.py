from pydantic import BaseModel

class ReadmissionResponse(BaseModel):
    prediction: str
    probability: float
    risk_level: str