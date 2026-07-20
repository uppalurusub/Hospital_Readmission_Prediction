from fastapi import APIRouter
from models.request_schema import ReadmissionRequest
from models.response_schema import ReadmissionResponse
from services.prediction_service import predict_readmission

router = APIRouter(
    prefix="/predict",
    tags=["Readmission Prediction"]
)

@router.post("/", response_model=ReadmissionResponse)
def predict(data: ReadmissionRequest):
    return predict_readmission(data)