# appl/services/user_service.py
from core.domain.user import User
from core.repositories.user_repository import UserRepository
from appl.dto.create_user_dto import CreateUserDTO


class UserService:

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create_user(self, dto: CreateUserDTO) -> User:
        user = User(
            id=None,
            name=dto.name,
            email=dto.email
        )

        return self.repository.save(user)

    def list_users(self) -> list[User]:
        return self.repository.list_all()