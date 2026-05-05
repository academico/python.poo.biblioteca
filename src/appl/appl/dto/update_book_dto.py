# appl/dto/update_book_dto.py
class UpdateBookDTO:
    def __init__(self, id: int, title: str, author: str, isbn: str, user_id: int | None = None):
        self.id = id
        self.title = title
        self.author = author
        self.isbn = isbn
        self.user_id = user_id