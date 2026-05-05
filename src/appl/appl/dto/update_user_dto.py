# appl/dto/update_user_dto.py
class UpdateUserDTO:
    def __init__(self, id: int, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email