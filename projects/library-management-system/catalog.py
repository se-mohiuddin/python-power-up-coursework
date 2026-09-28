#catalog
from books import Book
from patrons import Patron
from library import Library

class Catalog:
    def __init__(self, library):
        self.library = library

    def show_all_books(self):
        print("List of books in the library:\n")
        for book in self.library.books:
            print(f"Title: {book.title}, by: {book.author}")
            print(f"  Total copies: {book.total_copies}, Available copies: {book.available_copies}")
            print(f"  ISBN: {book.ISBN}")
            print("----------------------------------------------------------------------------")
        print("----------------------------------------------------------------------------")

    def show_all_patrons(self):
        print("List of patrons in the library:\n")
        for patron in self.library.patrons:
            print(f"Name: {patron.name}, Patron ID: {patron.patron_ID}")
            print("----------------------------------------------------------------------------")
        print("----------------------------------------------------------------------------")
            
    def show_borrowed_books(self):
        print("Borrowed books:\n")
        for patron in self.library.patrons:
            for borrowed_book in patron.books_borrowed:
                book = borrowed_book["book"]
                due_date = borrowed_book["due_date"]
                print(f"Title: {book.title}, Author: {book.author}")
                print(f"  Borrowed by: {patron.name}")
                print(f"  Due Date: {due_date}")
                print("----------------------------------------------------------------------------")

                # Check if there are reservations for this book
                queue = self.library.reservations[book]
                if queue:
                    print("  Reservations:")
                    for reserved_patron in queue:
                        print(f"  This book is reserved by: {reserved_patron.name}")
                    print("----------------------------------------------------------------------------")
        print("----------------------------------------------------------------------------")