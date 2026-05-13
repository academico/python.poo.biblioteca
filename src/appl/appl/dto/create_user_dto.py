# appl/dto/create_user_dto.py
class CreateUserDTO:
    def __init__(self, name: str, email: str):
        self.name = name.strip()
        self.email = email.strip()
