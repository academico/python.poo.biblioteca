# core/repositories/user_repository.py   -- interface
# deve ser implementado pela camada APP que decide qual db lib usar
from abc import ABC, abstractmethod
from core.domain.user import User


class UserRepository(ABC):

    @abstractmethod
    def save(self, user: User) -> User:
        pass

    @abstractmethod
    def list_all(self) -> list[User]:
        pass