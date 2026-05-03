class User:
    def __init__(self, id: int | None, name: str, email: str):
        if not name:
            raise ValueError("Nome é obrigatório")
        if "@" not in email:
            raise ValueError("Email inválido")

        self.id = id
        self.name = name
        self.email = email

    def __repr__(self) -> str:
        return f"User(id={self.id}, name='{self.name}', email='{self.email}')"