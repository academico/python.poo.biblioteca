# core/entities/tb_books.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from core.entities.base import Base  # Importa o mesmo Base 

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    isbn = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))

    # Relacionamento inverso: cada livro pertence a um usuário
    user = relationship("User", back_populates="books")
