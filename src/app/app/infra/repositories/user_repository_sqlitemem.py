from sqlalchemy import insert, select
from core.domain.user import User
from core.entities.tb_users import users_table, metadata
from core.repositories.user_repository import UserRepository
from app.infra.db.abstract_sqlalchemy_repository import (
    AbstractSqlAlchemyRepository,
)

class SqlAlchemyUserRepository(
    AbstractSqlAlchemyRepository, UserRepository
):

    def __init__(self):
        super().__init__()
        self._create_table()

    def _create_table(self):
        metadata.create_all(self.conn)

    def save(self, user: User) -> User:
        stmt = insert(users_table).values(
            name=user.name,
            email=user.email,
        )

        result = self.conn.execute(stmt)
        self.conn.commit()

        user.id = result.inserted_primary_key[0]
        return user

    def list_all(self) -> list[User]:
        stmt = select(
            users_table.c.id,
            users_table.c.name,
            users_table.c.email,
        )

        result = self.conn.execute(stmt)

        return [
            User(
                id=row.id,
                name=row.name,
                email=row.email,
            )
            for row in result.fetchall()
        ]