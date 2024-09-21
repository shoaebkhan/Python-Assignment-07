# models/book.py

class Book():
    book_id: int
    title: str
    author: str
    availability: bool

    def __init__(self, b_id: int, b_title: str, b_author: str, b_avl: bool) -> None:
        self.book_id=b_id
        self.title=b_title
        self.author=b_author
        self.availability=b_avl
        
    def __str__(self) -> str:
        return f"Book(ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Available: {self.availability})"        
