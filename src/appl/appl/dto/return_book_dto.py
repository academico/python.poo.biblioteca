# appl/dto/return_book_dto.py
class ReturnBookDTO:
    def __init__(self, user_id: int, book_id: int):
        self.user_id = user_id
        self.book_id = book_id