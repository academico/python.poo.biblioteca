from abc import ABC, abstractmethod
#from typing import Generic, TypeVar, List, Optional

#T = TypeVar("T")  # Tipo genérico para um DTO

class IBaseView(ABC):
    @abstractmethod
    def Run(self):
        """Cria ou atualiza um objeto no repositório."""
        pass