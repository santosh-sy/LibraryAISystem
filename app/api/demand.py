from fastapi import APIRouter, HTTPException
from app.services.demand_service import predict_demand, train_demand_model

router = APIRouter(prefix="/demand", tags=["Demand Prediction"])


@router.post("/train")
def train_model():
    mse = train_demand_model()
    return {
        "message": "Demand model trained successfully",
        "mse": mse
    }


@router.get("/{book_id}")
def predict(book_id: str):
    prediction = predict_demand(book_id)
    if prediction is None:
        raise HTTPException(status_code=404, detail="Book not found")

    return {
        "book_id": book_id,
        "predicted_review_count": prediction
    }
