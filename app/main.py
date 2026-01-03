from fastapi import FastAPI
from app.api.books import router as books_router
from app.api.recommendations import router as recommend_router
from app.api.demand import router as demand_router

app = FastAPI(title="Library AI System")

@app.get("/")
def health():
    return {"status": "ok"}

app.include_router(books_router)
app.include_router(recommend_router)
app.include_router(demand_router)