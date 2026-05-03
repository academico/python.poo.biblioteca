
# app/infra/repositories/in_memory_user_repository.py
from core.domain.user import User
from core.repositories.user_repository import UserRepository


class InMemoryUserRepository(UserRepository):

    def __init__(self):
        self._data: list[User] = []
        self._next_id = 1

    def save(self, user: User) -> User:
        user.id = self._next_id
        self._next_id += 1

        self._data.append(user)
        return user

    def list_all(self) -> list[User]:
        return list(self._data)
