# app/infra/repositories/in_memory_user_repository.py
from core.domain.user import User
from core.repositories.user_repository import IUserRepository


class InMemoryUserRepository(IUserRepository):
    def __init__(self):
        self._data: list[User] = []
        self._next_id = 1

    def save(self, user: User) -> User:
        """Cria um novo usuário e atribui ID sequencial."""
        user.id = self._next_id
        self._next_id += 1
        self._data.append(user)
        return user

    def update(self, user: User) -> User:
        """Atualiza um usuário existente pelo ID."""
        for idx, existing in enumerate(self._data):
            if existing.id == user.id:
                self._data[idx] = user
                return user
        raise ValueError(f"User with id={user.id} not found")

    def list_all(self) -> list[User]:
        """Retorna todos os usuários armazenados."""
        return list(self._data)

    def get_by_id(self, id: int) -> User | None:
        """Busca usuário pelo ID."""
        return next((u for u in self._data if u.id == id), None)

    def delete(self, id: int) -> None:
        """Remove usuário pelo ID."""
        self._data = [u for u in self._data if u.id != id]

    def exists(self, id: int) -> bool:
        """Verifica se usuário existe pelo ID."""
        return any(u.id == id for u in self._data)

    def count(self) -> int:
        """Retorna a quantidade total de usuários."""
        return len(self._data)

    def find_by(self, **kwargs) -> list[User]:
        """
        Busca usuários por atributos arbitrários.
        Exemplo: repo.find_by(name="Mauro")
        """
        results = []
        for u in self._data:
            if all(getattr(u, k) == v for k, v in kwargs.items()):
                results.append(u)
        return results
