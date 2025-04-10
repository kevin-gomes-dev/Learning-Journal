# LIBRARY CLASS
# For type hinting, remove imports and all hinting in demo for validations to work
from book import Book
from borrower import Borrower
class Library:
    def __init__(self):
        self.inventory: list[Book] = []
        
    def add_book(self,book: Book):
        self.inventory.append(book)
    
    def checkout_book(self,book: Book,borrower: Borrower):
        if book.available:
            book.available = False
            borrower.borrowed_books.append(book)
            self.inventory.remove(book)
        else:
            print(book.title + " is not available.")
    
    def return_book(self,book: Book,borrower: Borrower):
        if book in borrower.borrowed_books:
            book.available = True
            borrower.borrowed_books.remove(book)
            self.inventory.append(book)
        else:
            print(borrower.name + " didn't borrow " + book.title + ".")
    
    def list_available_books(self) -> list[str]:
        return [book.title for book in self.inventory if book.available]