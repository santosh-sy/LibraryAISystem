import pandas as pd
from app.db.mongodb import books_collection
from app.ml.demand_model import DemandModel

_model = DemandModel()
_trained = False

def train_demand_model():
    global _trained
    books = list(books_collection.find({}, {"_id": 0}))
    df = pd.DataFrame(books)

    mse = _model.train(df)
    _trained = True
    return mse

def predict_demand(book_id: str):
    if not _trained:
        train_demand_model()

    book = books_collection.find_one({"book_id": book_id}, {"_id": 0})
    if not book:
        return None

    features = {
        "genre": book["genre"],
        "year": book["year"],
        "price": book["price"],
        "rating": book["rating"],
    }

    return _model.predict(features)