# appl/dto/create_book_dto.py
class CreateBookDTO:
    def __init__(self, title: str, author: str, isbn: str, user_id: int | None = None):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.user_id = user_id