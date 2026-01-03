import pandas as pd
from app.db.mongodb import books_collection
from app.ml.recommender import BookRecommender

def get_recommendations(book_id: str):
    books = list(books_collection.find({}, {"_id": 0}))
    df = pd.DataFrame(books)

    recommender = BookRecommender(df)
    return recommender.recommend(book_id)
