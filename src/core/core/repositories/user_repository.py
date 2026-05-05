# core/repositories/user_repository.py   -- interface
# deve ser implementado pela camada APP que decide qual db lib usar

from core.domain.user import User
from core.repositories.base_repository import IBaseRepository

class IUserRepository(IBaseRepository[User]):
    """Interface específica para User, herdando os métodos genéricos."""
    pass