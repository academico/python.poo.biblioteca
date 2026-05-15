# appl/services/book_service.py
from core.core.domain.book import Book
from core.core.repositories.book_repository import IBookRepository
from core.core.repositories.user_repository import IUserRepository
from appl.dto.create_book_dto import CreateBookDTO
from appl.dto.update_book_dto import UpdateBookDTO

# Serviço faz injeção de dependencia dos repositórios book e usuário
# porque um livro pode ser emprestado por um usuário

class BookService:
    def __init__(self, book_repository: IBookRepository, user_repository: IUserRepository):
        self.book_repository = book_repository
        self.user_repository = user_repository

    def create_book(self, dto: CreateBookDTO) -> Book:
        if dto.user_id and not self.user_repository.exists(dto.user_id):
            raise ValueError(f"Usuário com id={dto.user_id} não encontrado")
            
        book = Book(id=None, title=dto.title, author=dto.author, isbn=dto.isbn, user_id=dto.user_id)
        return self.book_repository.save(book)

    def update_book(self, dto: UpdateBookDTO) -> Book:
        if not self.book_repository.exists(dto.id):
            raise ValueError(f"Livro com id={dto.id} não encontrado")

        if dto.user_id and not self.user_repository.exists(dto.user_id):
            raise ValueError(f"Usuário com id={dto.user_id} não encontrado")

        book = Book(id=dto.id, title=dto.title, author=dto.author, isbn=dto.isbn, user_id=dto.user_id)
        return self.book_repository.update(book)

    def list_books(self) -> list[Book]:
        return self.book_repository.list_all()

    def get_book_by_id(self, book_id: int) -> Book | None:
        return self.book_repository.get_by_id(book_id)

    def delete_book(self, book_id: int) -> None:
        if not self.book_repository.exists(book_id):
            raise ValueError(f"Livro com id={book_id} não encontrado")
        self.book_repository.delete(book_id)

    def count_books(self) -> int:
        return self.book_repository.count()

    def find_books_by_author(self, author: str) -> list[Book]:
        return self.book_repository.find_by(author=author)

    def find_books_by_title(self, title: str) -> list[Book]:
        return self.book_repository.find_by(title=title)
