from fastapi import APIRouter
from app.services.predict_service import predict_stock

router = APIRouter(prefix="/api")

@router.post("/predict")
def predict():
    return predict_stock()