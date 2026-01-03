class Book:
    def __init__(
        self,
        book_id: str,
        title: str,
        author: str,
        genre: str,
        rating: float,
        review_count: int,
        price: float,
        year: int
    ):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.rating = rating
        self.review_count = review_count
        self.price = price
        self.year = year