# src/app/app/infra/repositories/book_repository_sqlitemem.py

from sqlalchemy.orm import Session

from core.domain.book import Book
from core.repositories.book_repository import IBookRepository
from app.infra.persistence.common.mapper.mapper import Mapper
from app.infra.persistence.sqlalchemy.entities.book_entity import BookEntity
from app.infra.persistence.sqlalchemy.db.abstract_sqlalchemy_repository import AbstractSqlAlchemyRepository

class SqlAlchemyBookRepository(AbstractSqlAlchemyRepository, IBookRepository):
    """
    Implementação concreta de IBookRepository usando SQLAlchemy.
    """

    def __init__(self, session: Session) -> None:
        super().__init__(session)

    def save(self, book: Book) -> Book:
        entity = Mapper.to_entity(book, BookEntity)
        self.session.add(entity)
        self.session.commit()
        # Após commit, o SQLAlchemy preenche o ID gerado
        return Mapper.to_domain(entity, Book)

    def update(self, book: Book) -> Book:
        entity = self.session.get(BookEntity, book.id)
        if not entity:
            raise ValueError(f"Book with id={book.id} not found")
        # Atualiza os campos
        entity.title = book.title
        entity.author = book.author
        entity.isbn = book.isbn
        entity.user_id = book.user_id
        self.session.commit()
        return Mapper.to_domain(entity, Book)

    def list_all(self) -> list[Book]:
        entities = self.session.query(BookEntity).all()
        return [Mapper.to_domain(e, Book) for e in entities]

    def get_by_id(self, id: int) -> Book | None:
        entity = self.session.get(BookEntity, id)
        return Mapper.to_domain(entity, Book) if entity else None

    def delete(self, id: int) -> None:
        entity = self.session.get(BookEntity, id)
        if entity:
            self.session.delete(entity)
            self.session.commit()

    def exists(self, id: int) -> bool:
        return self.session.query(BookEntity).filter_by(id=id).first() is not None

    def count(self) -> int:
        return self.session.query(BookEntity).count()

    def find_by(self, **kwargs) -> list[Book]:
        entities = self.session.query(BookEntity).filter_by(**kwargs).all()
        return [Mapper.to_domain(e, Book) for e in entities]
