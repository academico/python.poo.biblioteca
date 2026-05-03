# appl/dto/create_user_dto.py
class CreateUserDTO:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
