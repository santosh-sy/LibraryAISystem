from pydantic import BaseModel

class Book(BaseModel):
    book_id: str
    title: str
    author: str
    rating: float
    review_count: int
    price: float
    year: int
    genre: str
