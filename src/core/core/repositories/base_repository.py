# core/repositories/base_repository.py
from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List, Optional

T = TypeVar("T")  # Tipo genérico para Domain

class IBaseRepository(ABC, Generic[T]):
    @abstractmethod
    def save(self, obj: T) -> T:
        """Cria ou atualiza um objeto no repositório."""
        pass

    @abstractmethod
    def update(self, obj: T) -> T:
        """Atualiza um objeto existente no repositório."""
        pass

    @abstractmethod
    def list_all(self) -> List[T]:
        """Retorna todos os objetos do repositório."""
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Optional[T]:
        """Busca um objeto pelo ID."""
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        """Remove um objeto pelo ID."""
        pass

    @abstractmethod
    def exists(self, id: int) -> bool:
        """Verifica se um objeto existe pelo ID."""
        pass

    @abstractmethod
    def count(self) -> int:
        """Retorna a quantidade total de objetos."""
        pass

    @abstractmethod
    def find_by(self, **kwargs) -> List[T]:
        """
        Busca objetos por atributos arbitrários.
        Exemplo: repo.find_by(name="Mauro", email="mauro@example.com")
        """
        pass