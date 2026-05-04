# core/entities/tb_users.py
#  Isso substitui o CREATE TABLE manual
# ✅ Não cria classes acopladas
# ✅ Pode ser reutilizado por múltiplos repositórios

from sqlalchemy import Table, Column, Integer, String, MetaData

metadata = MetaData()

users_table = Table(
    "users", #representa uma classe em domain
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String, nullable=False),
    Column("email", String, nullable=False),
)