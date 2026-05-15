# appl/services/user_service.py
from core.core.domain.user import User
from core.core.domain.book import Book
from core.core.repositories.user_repository import IUserRepository
from core.core.repositories.book_repository import IBookRepository
from appl.dto.create_user_dto import CreateUserDTO
from appl.dto.update_user_dto import UpdateUserDTO
from appl.dto.borrow_book_dto import BorrowBookDTO
from appl.dto.return_book_dto import ReturnBookDTO


class UserService:
    def __init__(self, user_repository: IUserRepository, book_repository: IBookRepository):
        self.user_repository = user_repository
        self.book_repository = book_repository

    def create_user(self, dto: CreateUserDTO) -> User:
        if self.user_repository.find_by(email=dto.email):
            raise ValueError(f"Já existe um usuário com o email {dto.email}")
        user = User(id=None, name=dto.name, email=dto.email)
        return self.user_repository.save(user)

    def update_user(self, dto: UpdateUserDTO) -> User:
        if not self.user_repository.exists(dto.id):
            raise ValueError(f"Usuário com id={dto.id} não encontrado")
        user = User(id=dto.id, name=dto.name, email=dto.email)
        return self.user_repository.update(user)

    def list_users(self) -> list[User]:
        return self.user_repository.list_all()

    def get_user_by_id(self, user_id: int) -> User | None:
        return self.user_repository.get_by_id(user_id)

    def delete_user(self, user_id: int) -> None:
        if not self.user_repository.exists(user_id):
            raise ValueError(f"Usuário com id={user_id} não encontrado")
        self.user_repository.delete(user_id)

    def count_users(self) -> int:
        return self.user_repository.count()

    def find_users_by_name(self, name: str) -> list[User]:
        return self.user_repository.find_by(name=name)

    def find_users_by_email(self, email: str) -> list[User]:
        return self.user_repository.find_by(email=email)

    # --- Métodos de empréstimo ---
    def borrow_book(self, dto: BorrowBookDTO) -> Book:
        user = self.user_repository.get_by_id(dto.user_id)
        if not user:
            raise ValueError(f"Usuário com id={dto.user_id} não encontrado")

        book = self.book_repository.get_by_id(dto.book_id)
        if not book:
            raise ValueError(f"Livro com id={dto.book_id} não encontrado")

        if book.user_id is not None:
            raise ValueError(f"Livro {book.id} já está emprestado para outro usuário")

        book.user_id = user.id
        return self.book_repository.update(book)

    def return_book(self, dto: ReturnBookDTO) -> Book:
        user = self.user_repository.get_by_id(dto.user_id)
        if not user:
            raise ValueError(f"Usuário com id={dto.user_id} não encontrado")

        book = self.book_repository.get_by_id(dto.book_id)
        if not book:
            raise ValueError(f"Livro com id={dto.book_id} não encontrado")

        if book.user_id != user.id:
            raise ValueError(f"O livro {book.id} não está emprestado para o usuário {user.id}")

        book.user_id = None
        return self.book_repository.update(book)
