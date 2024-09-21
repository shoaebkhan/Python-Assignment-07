# models/librarian.py

from models.user import User    # type: ignore
from models.member import Member
from models.book import Book

class Librarian(User):
    def __init__(self, id: int, name: str, email: str)->None:
        super().__init__(id,name, email )

    def issue_book(self, member: Member, book: Book)->bool:
        if book.availability:
            book.availability = False
            return True
        return False
    
    def return_book(self, memeber: Member, book: Book)->bool:
        if not book.availability:
            book.availability = True
            return True
        return False
    
    def __str__(self) -> str:
        return f"Librarian(ID: {self.user_id}, Name: {self.name}, Email: {self.email})"