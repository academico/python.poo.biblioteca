class UserFilterDTO:
    def __init__(self, id: int | None = None, name: str | None = None, email: str | None = None):
        self.id = id
        self.name = name
        self.email = email

    def to_kwargs(self) -> dict:
        kwargs = {}
        if ((self.id is not None) and (self.id>0)):
            kwargs["id"] = self.id
        if self.name:
            kwargs["name"] = self.name
        if self.email:
            kwargs["email"] = self.email
        return kwargs