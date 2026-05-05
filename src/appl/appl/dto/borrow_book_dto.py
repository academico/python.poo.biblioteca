# appl/dto/borrow_book_dto.py
class BorrowBookDTO:
    def __init__(self, user_id: int, book_id: int):
        self.user_id = user_id
        self.book_id = book_id