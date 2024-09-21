# models/user.py
class User:
    user_id: int
    name: str
    email: str

    def __init__(self, id: int, name: str, email:str) -> None:
        self.user_id = id
        self.name = name
        self.email = str.lower(email)
    