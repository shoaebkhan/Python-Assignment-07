from models.user import User
from models.member import Member
from models.book import Book
from models.librarian import Librarian
import pickle
from typing import List, TypeVar
T= TypeVar('T')

class LibraryManager(User):
    members_list: list[User]
    books_list: list[Book]
    librarians_list: list[User]

    def __init__(self, id: int, name: str, email: str) -> None:
        super().__init__(id, name, email)
        self.members_list = []
        self.books_list = []
        self.librarians_list = []    
 
    def read_objects_from_file(self, file_name: str, mode: str)->List[T]:
        objects_list: List[T] = []
        with open(file_name, mode) as file:
            while True:
                try:
                    obj = pickle.load(file)
                    objects_list.append(obj)
                except EOFError:
                    break
        return objects_list

    def write_objects_to_file(self, file_name: str, mode: str, objects: List[T]):
        with open(file_name, mode) as file:
            for obj in objects:
                pickle.dump(obj, file)

    def write_object_to_file(self, file_name: str, mode: str, object: T):
        with open(file_name, mode) as file:
            pickle.dump(object, file)

    def set_books_list(self):
        self.books_list = self.read_objects_from_file('books.pkl', 'rb')
        if len(self.books_list)> 0: 
            return
        else:
            # Sample data for titles and authors
            titles = [
                "The Great Gatsby", "To Kill a Mockingbird", "1984", "Pride and Prejudice", 
                "The Catcher in the Rye", "Moby-Dick", "War and Peace", "The Odyssey",
                "The Hobbit", "Crime and Punishment", "Brave New World", "The Scarlet Letter", 
                "The Brothers Karamazov", "Frankenstein", "Dracula", "The Divine Comedy", 
                "Les Misérables", "Anna Karenina", "The Picture of Dorian Gray", "Hamlet"
            ]

            authors = [
                "F. Scott Fitzgerald", "Harper Lee", "George Orwell", "Jane Austen",
                "J.D. Salinger", "Herman Melville", "Leo Tolstoy", "Homer",
                "J.R.R. Tolkien", "Fyodor Dostoevsky", "Aldous Huxley", "Nathaniel Hawthorne",
                "Fyodor Dostoevsky", "Mary Shelley", "Bram Stoker", "Dante Alighieri",
                "Victor Hugo", "Leo Tolstoy", "Oscar Wilde", "William Shakespeare"
            ]

            # Generate a list of 20 Book objects
            for i in range(len(titles)):
                book = Book(i+1, titles[i], authors[i], True)
                self.librarians_list.append(book)
            self.write_objects_to_file('books.pkl', 'ab', self.books_list)
        return

    def set_librarians_list(self):
        self.librarians_list = self.read_objects_from_file('librarians.pkl', 'rb')
        if len(self.librarians_list)> 0: 
            return
        else:
            # List of names
            names = ["John", "Jane", "Alice"]
            # Generate a list of emails using a list comprehension
            emails = [f"{name.lower()}@example.com" for name in names]
            # Generate a list of 20 Librarian objects
            for i in range(len(names)):
                librarian = Librarian(i+1, names[i], emails[i])
                self.librarians_list.append(librarian)
            self.write_objects_to_file('librarians.pkl', 'ab', self.librarians_list)
        return

    def set_members_list(self):
        self.members_list = self.read_objects_from_file('members.pkl', 'rb')
        if len(self.members_list)> 0: 
            return
        else:
            names = ["Alice", "Bob", "Charlie", "David", "Eve"]
            # Generate a list of emails using a list comprehension
            emails = [f"{name.lower()}@gmail.com" for name in names]
            for i in range(len(names)):
                member = Member(i+1, names[i], emails[i])
                self.members_list.append(member)
            self.write_objects_to_file('members.pkl', 'ab', self.members_list)
        return

    def get_book_list(self)->list[Book]:
        if len(self.books_list):
            return self.books_list
        return []

    def get_librarians_list(self)->list[User]:
        if len(self.librarians_list):
            return self.librarians_list
        return []

    def get_members_list(self)->list[User]:
        if len(self.members_list):
            return self.members_list
        return []

#---------------------------CRUD for Members in the Library
    
    def create_member(self):
        name = input("Enter Member Name: ")
        email = input("Enter Member Email: ")
        id: int = 0
        if len(self.members_list) > 0:
            id = self.members_list[-1].user_id +1
        member = Member(id, name, email)
        self.members_list.append(member)
        self.write_object_to_file('members.pkl', 'ab', member)
        print(f"Member  Account with ID: {member.user_id} is created successfully..!")

    def retrieve_members(self):
        print(f"Total Members in the Library: {len(self.get_members_list())}")
        print([str(m) for m in self.members_list])

    def retrieve_member(self, mem_id: int)->Member:
        return self.search_member(mem_id)
    
    def update_member(self)->bool:
        print("Update Library Member-:- ")
        user_id = int(input("Enter Member ID: "))
        u = self.search_member(user_id)
        if isinstance(u, Member):
            name = input("Enter Member Name: ")
            email = input("Enter Member Email: ")
            u.name = name
            u.email = email
            self.write_objects_to_file('members.pkl', 'wb', self.members_list)
            print(f"Member Account with ID: {u.user_id} is updated successfully..!")
            return True 
        else:
            return False

    def delete_member(self)->bool:
        user_id = int(input("Enter Member ID: "))
        u = self.search_member(user_id)
        if u:
            self.members_list.remove(u)
            self.write_objects_to_file('members.pkl', 'wb', self.members_list)
            print(f"Member Account with ID: {user_id} is deleted successfully..!")
            return True
        else:
            return False

    def search_member(self, user_id:int):
        try:
            user = next(librarian for librarian in self.members_list if librarian.user_id == user_id)
            return user
        except StopIteration:
            print(f"No such member account found against {user_id}!")
            return None

#---------------------------CRUD for Librarian in the Library

    def create_librarian(self):
        name = input("Enter Librarian Name: ")
        email = input("Enter Librarian Email: ")
        id: int
        if len(self.librarians_list) > 0:
            id = self.librarians_list[-1].user_id +1
        else:
            id = 0
        librarian = Librarian(id, name, email)
        self.librarians_list.append(librarian)
        self.write_object_to_file('librarians.pkl', 'ab', librarian)
        print(f"Librarian Account with ID: {librarian.user_id} is created successfully..!")
        return

    def retrieve_Librarians(self)->None:
        print(f"Total Librarian in the Library: {len(self.get_librarians_list())}")
        print([str(l) for l in self.librarians_list])

    def retrieve_Librarian(self, lib_id)->Librarian:
        return self.search_librarian(lib_id)
    
    def update_librarian(self)->bool:
        print("Update Library Librarian-:- ")
        lib_id = int(input("Enter Librarian ID: "))
        u = self.search_librarian(lib_id)
        if isinstance(u, User):
            name = input("Enter User Name: ")
            email = input("Enter User Email: ")
            u.name = name
            u.email = email
            self.write_objects_to_file('librarians.pkl', 'wb', self.librarians_list)
            print(f"Librarian Account with ID: {u.user_id} is updated successfully")
            return True
        else:
           return False

    def delete_librarian(self)->bool:
        print("Remove Librarian-:- ")
        lib_id = int(input("Enter Librarian ID: "))
        u = self.search_librarian(lib_id)
        if u:
            self.librarians_list.remove(u)
            self.write_objects_to_file('librarians.pkl', 'wb', self.librarians_list)
            print(f"Librarian Account with ID: {lib_id} is deleted successfully")
            return True
        else:
            return False

    def search_librarian(self, lib_id:int):
        try:
            user = next(librarian for librarian in self.librarians_list if librarian.user_id == lib_id)
            return user
        except StopIteration:
            print(f"No such librarian account found against {lib_id}!") 
            return None

#---------------------------CRUD for Books in the Library
    def create_book(self)->bool:
        title = input("Enter Book Title: ")
        author = input("Enter Book Author: ")
        avlbl = self.inputBoolean()
        id = self.books_list[len(self.books_list)-1].book_id+1
        book = Book(id, title, author, avlbl)
        self.books_list.append(book)
        self.write_object_to_file('books.pkl', 'ab', book)
        print(f"Books with title {title} is successfully added to the library")
        return True

    def retrieve_Books(self)->None:
        print(f"Total Books in the Library: {len(self.get_book_list())}")
        print([str(b) for b in self.books_list])
    
    def retrieve_Book(self, book_id)->Book:
        return self.search_book(book_id)
    
    def update_book(self):
        print("Update Book in Library-:- ")
        book_id = int(input("Enter Book ID: "))
        b = self.search_book(book_id)
        if isinstance(b, Book):
            title = input("Enter Book Title: ")
            author = input("Enter Book Author: ")
            b.title = title
            b.author = author
            b.availability =self.inputBoolean()
            self.write_objects_to_file('books.pkl', 'wb',self.books_list)
            print(f"Book with title {title} is updated successfully.")
            return True
        else:
            return False
    
    def delete_book(self)->bool:
        book_id = int(input("Enter Book ID: "))
        book = self.search_book(book_id)
        if book:
            self.books_list.remove(book)
            self.write_objects_to_file('books.pkl', 'wb', self.books_list)
            print(f"Book with title {book_id} is deleted successfully.")
            return True
        else:
            return False
    
    def search_book(self, book_id: int):
        try:
            book = next(book for book in self.books_list if book.book_id == book_id)
        except StopIteration:
            print(f"Book with title {book_id} is not found in the library.")
            return book
    
    def __str__(self) -> str:
        return f"Library Manager(ID: {self.user_id}, Name: {self.name}, Email: {self.email})"

    def inputBoolean(self)->bool:
        avl = input("Availability: True | False: ")
        avlbl: bool
        if avl.lower() == "true":
            avlbl = True
        elif avl.lower() == "false":
            avlbl = False
        else:
            return False
        return avlbl    