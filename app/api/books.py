from fastapi import APIRouter, HTTPException
from typing import List
from app.db.mongodb import books_collection
from app.schemas.book import Book

router = APIRouter(prefix="/books", tags=["Books"])

@router.get("/", response_model=List[Book])
def get_books():
    return list(books_collection.find({}, {"_id": 0}))

@router.get("/{book_id}", response_model=Book)
def get_book(book_id: str):
    book = books_collection.find_one(
        {"book_id": book_id},
        {"_id": 0}
    )
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book
