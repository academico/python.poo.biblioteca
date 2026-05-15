# src/app/app/infra/repositories/sqlalchemy_user_repository.py

from sqlalchemy.orm import Session
from sqlalchemy import or_
from core.core.domain.user import User
from core.core.repositories.user_repository import IUserRepository
from app.infra.persistence.common.mapper.mapper import Mapper
from app.infra.persistence.sqlalchemy.entities.user_entity import UserEntity
from app.infra.persistence.sqlalchemy.db.abstract_sqlalchemy_repository import AbstractSqlAlchemyRepository

class SqlAlchemyUserRepository(AbstractSqlAlchemyRepository, IUserRepository):
    """
    Implementação concreta de IUserRepository usando SQLAlchemy.
    """

    def __init__(self, session: Session) -> None:
        super().__init__(session)

    def save(self, user: User) -> User:
        entity = Mapper.to_entity(user, UserEntity)
        self.session.add(entity)
        self.session.commit()
        # Após commit, o SQLAlchemy preenche o ID gerado
        return Mapper.to_domain(entity, User)

    def update(self, user: User) -> User:
        entity = self.session.get(UserEntity, user.id)
        if not entity:
            raise ValueError(f"User with id={user.id} not found")
        # Atualiza os campos
        entity.name = user.name
        entity.email = user.email
        self.session.commit()
        return Mapper.to_domain(entity, User)

    def list_all(self) -> list[User]:
        entities = self.session.query(UserEntity).all()
        return [Mapper.to_domain(e, User) for e in entities]

    def get_by_id(self, id: int) -> User | None:
        entity = self.session.get(UserEntity, id)
        return Mapper.to_domain(entity, User) if entity else None

    def delete(self, id: int) -> None:
        entity = self.session.get(UserEntity, id)
        if entity:
            self.session.delete(entity)
            self.session.commit()

    def exists(self, id: int) -> bool:
        return self.session.query(UserEntity).filter_by(id=id).first() is not None

    def count(self) -> int:
        return self.session.query(UserEntity).count()

    def find_by(self, **kwargs) -> list[User]:
        query = self.session.query(UserEntity)
        name = kwargs.pop("name", None)
        email = kwargs.pop("email", None)
        filters = []
        if name:
            filters.append(UserEntity.name.ilike(f"%{name}%"))
        if email:
            filters.append(UserEntity.email.ilike(f"%{email}%"))
        if filters:
            query = query.filter(or_(*filters))

        # Para os demais kwargs (igualdade exata)
        if kwargs:
            query = query.filter_by(**kwargs)

        entities = query.all()
        return [Mapper.to_domain(e, User) for e in entities]
