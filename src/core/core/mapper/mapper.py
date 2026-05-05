# core/mappers/generic_mapper.py

class Mapper:
    @staticmethod
    def asdict(obj) -> dict:
        """
        Converte qualquer objeto em dict usando __dict__,
        ignorando atributos internos do SQLAlchemy (_sa_instance_state).
        """
        return {
            k: v for k, v in vars(obj).items()
            if not k.startswith("_")
        }

    @staticmethod
    def from_dict(cls, data: dict):
        """
        Cria uma instância da classe a partir de um dict.
        """
        return cls(**data)

    @classmethod
    def to_domain(cls, entity, domain_cls):
        """
        Converte uma Entity (ORM) para Domain.
        """
        data = cls.asdict(entity)
        return cls.from_dict(domain_cls, data)

    @classmethod
    def to_entity(cls, domain, entity_cls):
        """
        Converte um Domain para Entity (ORM).
        """
        data = cls.asdict(domain)
        return cls.from_dict(entity_cls, data)
