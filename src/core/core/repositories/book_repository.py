# core/repositories/user_repository.py   -- interface
# deve ser implementado pela camada APP que decide qual db lib usar

from core.domain.book import Book
from core.repositories.base_repository import IBaseRepository

class IBookRepository(IBaseRepository[Book]):
    """Interface específica para Book, herdando os métodos genéricos."""
    pass