# core/entities/book_entity.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base  # Importa o mesmo Base 

class BookEntity(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    isbn = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id")) #"<table>.id"

    # Relacionamento inverso: cada livro pertence a um usuário
    user = relationship("UserEntity", back_populates="books")
