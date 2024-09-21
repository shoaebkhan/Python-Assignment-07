from typing import Optional
from models.library_manager import LibraryManager
from models.librarian import Librarian
from models.member import Member
from models.book import Book
import os


class LMS:
    lm: LibraryManager
    
    def __init__(self, id: int = 1, name: str ="Ali", email: str ="Ali@gmail.com") -> None:
        self.lm = LibraryManager(id, name, email)
        self.lm.set_librarians_list()
        self.lm.set_members_list()
        self.lm.set_books_list()

    def verify_lm_credentials(self, email: str)->bool:
        if email == self.lm.email:
            return True
        else:
            return False
    
    def user_selection(self, min: int, max: int)->int:
        option = int(input("Enter your option: "))
        while not (option >= min and option <= max):
            print("Invalid option, please enter again")
            option = int(input("Enter your option: "))
        os.system('cls')
        return option
    
    def manage_librarian_accounts(self)->None:
        os.system('cls')
        print("-------------- Manage Librarians Menu -------------")
        print("Welcom to Library Management System")
        print("\n1. Create Librarian Account\n2. Update Librarian Account\n3. Delete Librarian Account\n4. Search Librarian\n5. Display all\n6. Back")
        option = self.user_selection(1, 6)
        if option == 1:
            self.lm.create_librarian()
        elif option == 2:
            self.lm.update_librarian()
        elif option == 3:
            self.lm.delete_librarian()
        elif option == 4:
            lib_id = int(input("Enter Librarian ID: "))
            lib = self.lm.search_librarian(lib_id)
            print(str(lib))
        elif option == 5:
            self.lm.retrieve_Librarians()
        elif option == 6:
            self.library_mgr_menu()
        input("Press any key to continue...")
        os.system('cls')
        self.manage_librarian_accounts()
        return
    
    def manage_member_accounts(self)->None:
        os.system('cls')
        print("-------------- Manage Members Menu -------------")
        print("Welcom to Library Management System")
        print("\n1. Create Member Account\n2. Update Member Account\n3. Delete Member Account\n4. Search Member\n5. Display all\n6. Back")
        option = self.user_selection(1, 6)
        if option == 1:
            self.lm.create_member()
        elif option == 2:
            self.lm.update_member()
        elif option == 3:
            self.lm.delete_member()
        elif option == 4:
            mem_id = int(input("Enter Book ID: "))
            mem = self.lm.search_member(mem_id)
            print(str(mem))
        elif option == 5:
            self.lm.retrieve_members()
        elif option == 6:
            self.library_mgr_menu()
        input("Press any key to continue...")
        os.system('cls')
        self.manage_member_accounts()
        return

    def manage_books(self)->None:
        print("-------------- Manage Books -------------")
        os.system('cls')
        print("Welcom to Library Management System")
        print("\n1. Add Book \n2. Update Book Information\n3. Delete Book\n4. Search Book\n5. Display all\n6. Back")
        option = self.user_selection(1, 6)
        if option == 1:
            self.lm.create_book()
        elif option == 2:
            self.lm.update_book()
        elif option == 3:
            self.lm.delete_book()
        elif option == 4:
            book_id = int(input("Enter Book ID: "))
            book = self.lm.search_book(book_id)
            print(str(book))
        elif option == 5:
            self.lm.retrieve_Books()
        elif option == 6:
            self.library_mgr_menu()
        input("Press any key to continue...")
        os.system('cls')
        self.manage_books()

    def main_menu(self):
        os.system('cls')
        print("-------------- Main Menu -------------")
        print("Welcom to Library Management System")
        print("\n1. Login\n2.Signup\n3. Exit")
        option = self.user_selection(1, 3)
        if option == 1:
            self.login_menu()
        elif option == 2:
            self.signup_menu()
        elif option == 3:
            return
    
    def signup_menu(self):
        return

    def login_menu(self):
        os.system('cls')
        print("-------------- Login Menu -------------")
        print("Welcom to Library Management System")
        print("\n1. Library Manager Login\n2. Librarian Login\n3. Member Login\n4. Main Menu")
        option = self.user_selection(1, 4)
        os.system('cls')
        if option == 1:
            self.library_mgr_login()
        elif option == 2:
            self.librarian_login()
        elif option == 3:
            self.member_login()
        elif option == 4:
            self.main_menu()
    
    def library_mgr_menu(self):
        os.system('cls')
        print(f"\t\t\t\t [You are Logged in as: {self.lm.name}]")
        print("-------------- Library Manager Menu -------------")
        print("Welcom to Library Management System")
        print("\n1. Manage Librarians\n2. Manager Members\n3. Manage Books\n4. Logout")
        option = self.user_selection(1, 4) 
        #------- Manage Librarian Account----------------
        if option == 1:
            self.manage_librarian_accounts()
        #------- Manage Member Account----------------
        elif option == 2:
            self.manage_member_accounts()
        #------- Manage Books----------------
        elif option == 3:
            self.manage_books()
        elif option == 4:
            self.main_menu()

    def library_mgr_login(self): 
        print("-------------- Library Manager Login -------------")
        print("Welcom to Library Management System")
        email = input("Enter your email to login: ")
        status = self.verify_lm_credentials(email)
        if status:
            self.library_mgr_menu()
        else:
            print("Invalid Credentials provided..!")
            input("Press any key to continue...")
            os.system('cls')
            self.library_mgr_login()
        
    def librarian_login(self):
        print("-------------- Librarian Login -------------")
        print("Welcom to Library Management System")
        email = input("Enter your email to login: ")
        try:
            lib = next(lib for lib in self.lm.get_librarians_list() if lib.email == email )            
            if isinstance(lib, Librarian):
                self.librarian_menu(lib)
        except StopIteration:
            print("Invalid Credentials provided..!")
            input("Press any key to continue...")
            os.system('cls')
            self.librarian_login()
        return
    
    def librarian_menu(self, lib: Librarian):
        os.system('cls')
        print("-------------- Librarian Menu -------------")
        print(f"\t\t\t\t [You are Logged in as: {lib.name}]")
        print("Welcom to Library Management System")
        print("\n1. Issue Book\n2. Return Book\n3. Logout")
        option = self.user_selection(1, 3) 
        #------- Issue Book to Member----------------
        if option == 1:
            mem = self.input_mem_info()
            book = self.input_book_info()
            status = self.issue_book_to(book, mem, lib)
            if status:
                print("Book issued successfully..!!")
                print(f"Book with ID: {book.book_id} is issue to {mem.user_id} by Librarian {lib.user_id}")
                input("Press any key to continue...")
                os.system('cls')
                self.librarian_menu(lib)
            else:
                print(f"Error\nUnable to issue book: {book.book_id} to member: {mem.user_id}!")
                input("Press any key to continue...")
                os.system('cls')
                self.librarian_menu(lib)
        #------- Return Book from a Member----------------
        elif option == 2:
            mem = self.input_mem_info()
            book = self.input_book_info()
            status = self.return_book_from(book, mem, lib)
            if status:
                print("Book returned successfully..!!")
                print(f"Book with ID: {book.book_id} is returned from {mem.user_id} by Librarian {lib.user_id}")
                input("Press any key to continue...")
                os.system('cls')
                self.librarian_menu(lib)
            else:
                print(f"Error\nUnable to return book: {book.book_id} from member: {mem.user_id}!")
                input("Press any key to continue...")
                os.system('cls')
                self.librarian_menu(lib)
        #------- return back to Login Menu----------------
        elif option == 3:
            self.login_menu()
        return
    
    def input_mem_info(self)->Member:
        email = input("Enter member email: ")
        mem = next(mem for mem in self.lm.get_members_list() if email == mem.email)
        while not isinstance(mem, Member):
            print("Invalid Credentials provided..!")
            input("Press any key to continue...")
            os.system('cls')
            email = input("Enter member email again: ")
            mem = next(mem for mem in self.lm.get_members_list() if email == mem.email)
        return mem

    def input_book_info(self)->Book:
        book_id = int(input("Enter Book ID: "))
        book = next(book for book in self.lm.get_book_list() if book_id == book.book_id)
        while not isinstance(book, Book):
            print("Invalid Book ID provided..!")
            input("Press any key to continue...")
            os.system('cls')
            book_id = int(input("Enter Book ID: "))
            book = next(book for book in self.lm.get_book_list() if book_id == book.book_id)
        return book

    def issue_book_to(self, book: Book, mem: Member, lib: Optional[Librarian])->bool:
        if lib is None:
            return mem.issue_book(book)
        else:
            return lib.issue_book(mem, book )
    
    def return_book_from(self, book: Book, mem: Member, lib: Optional[Librarian])->bool:
        if lib is None:
            return mem.return_book(book)
        else:
            return lib.return_book(mem, book)

    def member_login(self):
        print("-------------- Member Login -------------")
        print("Welcom to Library Management System")
        mem = self.input_mem_info()
        try:
            if isinstance(mem, Member):
                self.member_menu(mem)
        except StopIteration:
            print("Invalid Credentials provided..!")
            input("Press any key to continue...")
            os.system('cls')
            self.member_login()
        return
    
    def member_menu(self, mem: Member):
        os.system('cls')
        print("-------------- Member Menu -------------")
        print(f"\t\t\t\t [You are Logged in as: {mem.name}]")
        print("Welcom to Library Management System")
        print("\n1. Issue Book\n2. Return Book\n3. Logout")
        option = self.user_selection(1, 3) 
        #------- Issue Book to Member----------------
        if option == 1:
            book = self.input_book_info()
            status = self.issue_book_to(book, mem, None)
            if status:
                
                print("Book issued successfully..!!")
                print(f"Book with ID: {book.book_id} is issue to {mem.user_id}")
                input("Press any key to continue...")
                os.system('cls')
                self.member_menu(mem)
            else:
                print(f"Error\nUnable to issue book: {book.book_id} to member: {mem.user_id}!")
                input("Press any key to continue...")
                os.system('cls')
                self.member_menu(mem)
        #------- Return Book from a Member----------------
        elif option == 2:
            book = self.input_book_info()
            status = self.return_book_from(book, mem, None)
            if status:
                print("Book returned successfully..!!")
                print(f"Book with ID: {book.book_id} is returned by {mem.user_id}")
                input("Press any key to continue...")
                os.system('cls')
                self.member_menu(mem)
            else:
                print(f"Error\nUnable to return book: {book.book_id} from member: {mem.user_id}!")
                input("Press any key to continue...")
                os.system('cls')
                self.member_menu(mem)
        #------- return back to Login Menu----------------
        elif option == 3:
            self.login_menu()
        return