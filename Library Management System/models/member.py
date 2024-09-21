from models.book import Book
from models.user import User

class Member(User):
    def __init__(self, id: int, name: str, email: str)->None:
        super().__init__(id,name, email )

    def issue_book(self, book: Book):
        if book.availability:
            book.availability = False
            return True
        return False
    
    def return_book(self, book: Book):
        if  book.availability:
            book.availability = True
            return True
        return False
    def __str__(self) -> str:
        return f"Member(ID: {self.user_id}, Name: {self.name}, Email: {self.email})"