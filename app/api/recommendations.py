from fastapi import APIRouter, HTTPException
from app.services.recommendation_service import get_recommendations

router = APIRouter(prefix="/recommend", tags=["Recommendations"])

@router.get("/{book_id}")
def recommend_books(book_id: str):
    recommendations = get_recommendations(book_id)
    if not recommendations:
        raise HTTPException(status_code=404, detail="Book not found")
    return recommendations
