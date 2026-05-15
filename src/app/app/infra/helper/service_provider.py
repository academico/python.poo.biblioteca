from typing import TypeVar, Dict, Type
T = TypeVar("T")

class ServiceProvider:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._services: Dict[Type, object] = {}
        return cls._instance

    def Registry(self, service: object) -> None:
        """Registra uma instância de serviço"""
        self._services[type(service)] = service

    def Get(self, service_type: Type[T]) -> T:
        """Recupera o serviço pela classe"""
        return self._services.get(service_type)  # type: ignore

    def __getitem__(self, service_type: Type[T]) -> T:
        """Permite usar provider[ServiceType]"""
        return self.Get(service_type)