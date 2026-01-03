import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from app.schemas.book import Book


class BookRecommender:
    def __init__(self, df: pd.DataFrame):
        self.df = df.reset_index(drop=True)
        self.vectorizer = TfidfVectorizer(stop_words="english")

        self.df["features"] = (
            self.df["title"] + " " + self.df["author"] + " " + self.df["genre"]
        )

        self.matrix = self.vectorizer.fit_transform(self.df["features"])

    def recommend(self, book_id: str, top_n: int = 5):
        idx = self.df.index[self.df["book_id"] == book_id].tolist()
        if not idx:
            return []
        idx = idx[0]
        scores = cosine_similarity(self.matrix[idx], self.matrix).flatten()
        top_indices = scores.argsort()[::-1][1:top_n + 1]

        return self.df.iloc[top_indices].to_dict(orient="records")

