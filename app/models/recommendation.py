class Recommendation:
    def __init__(self, source_book_id: str, recommended_book_id: str, score: float):
        self.source_book_id = source_book_id
        self.recommended_book_id = recommended_book_id
        self.score = score