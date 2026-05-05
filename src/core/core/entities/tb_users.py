# core/entities/tb_users.py
#  Isso substitui o CREATE TABLE manual
# ✅ Não cria classes acopladas
# ✅ Pode ser reutilizado por múltiplos repositórios

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, relationship
from core.entities.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

    # Relacionamento: um usuário pode emprestar vários livros
    books = relationship("Book", back_populates="user")
