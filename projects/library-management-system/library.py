#library
from books import Book 
from patrons import Patron
import datetime
from collections import defaultdict, deque
import pickle

class Library:
    def __init__(self):
        self.books= []
        self.patrons= []
        self.reservations = defaultdict(deque) # Use defaultdict with a queue as the default value

    def add_book(self, book):
        self.books.append(book)
        print("The book is successfully added in library")
        print("----------------------------------------------------------------------------")

    def add_patron(self, patron):
        self.patrons.append(patron)
        print("The patron is successfully added in library")
        print("----------------------------------------------------------------------------")

    def borrow_book(self, patron, book):
        borrowed_books = [item["book"] for item in patron.books_borrowed]

        if book in borrowed_books:
            print("Patron has already borrowed this book.")
            print("----------------------------------------------------------------------------")
        else:
            if book.available_copies > 0:
                due_date = datetime.datetime.now() + datetime.timedelta(days=14)  # Set due date as 2 weeks from now
                patron.books_borrowed.append({"book": book, "due_date": due_date})
                book.available_copies -= 1
                print(f"{patron.name} has borrowed {book.title} book.\n Due date: {due_date}.")
                print("----------------------------------------------------------------------------")
            else:
                print("Sorry, all copies of this book are currently borrowed.")
                print("----------------------------------------------------------------------------")

    def reserve_book(self, patron, book):
        borrowed_books = [item["book"] for item in patron.books_borrowed]
        
        if book in borrowed_books:
            print("You can't reserve a book you've already borrowed.")
            print("----------------------------------------------------------------------------")
        else:
            self.reservations[book].append(patron)  # Add the patron to the reservation queue for the book
            if len(self.reservations[book]) == 1:
                print(f"{patron.name} has reserved {book.title}.")
                print("----------------------------------------------------------------------------")
            else:
                position = len(self.reservations[book])
                print(f"{patron.name} has reserved {book.title}. Position in queue: {position}.")
                print("----------------------------------------------------------------------------")

    def return_book(self, patron, book):
        borrowed_book_entry = next((item for item in patron.books_borrowed if item["book"] == book), None)

        if borrowed_book_entry:
            due_date = borrowed_book_entry["due_date"]
            return_date = datetime.datetime.now()
            if return_date > due_date:
                overdue_days = (return_date - due_date).days
                overdue_fine = overdue_days * 2  # Example: $2 per day
                print(f"Overdue: {overdue_days} days. Overdue fine: ${overdue_fine}")

            patron.books_borrowed.remove(borrowed_book_entry)
            book.available_copies += 1
            print(f"{patron.name} has returned {book.title}.")
            print("----------------------------------------------------------------------------")

            if self.reservations[book]:
                next_patron = self.reservations[book].popleft()
                if self.reservations[book]:
                    second_patron = self.reservations[book][0]
                    print(f"Book '{book.title}' is now available. \n{next_patron.name} is next in the queue and can borrow it now.")
                    print(f"{second_patron.name} is now second in the queue.")
                    print("----------------------------------------------------------------------------")
                    print("----------------------------------------------------------------------------")
                else:
                    print(f"Book '{book.title}' returned. \n{next_patron.name} is next in the queue and can borrow it now.")
                    print("----------------------------------------------------------------------------")
                    print("----------------------------------------------------------------------------")
            else:
                print("No reservations at the moment.")
                print("----------------------------------------------------------------------------")
                print("----------------------------------------------------------------------------")
        else:
            print("Patron has not borrowed this book.")
            print("----------------------------------------------------------------------------")

    def save_data(self, filename):
        with open(filename, 'wb') as f:
            data = {"books": self.books, "patrons": self.patrons}
            pickle.dump(data, f)
            print("Library data  saved successfully!")
            print("----------------------------------------------------------------------------")

    def load_data(self, filename):
        with open(filename, 'rb') as f:
            data = pickle.load(f)
            self.books = data["books"]
            self.patrons = data["patrons"]
            print("Library data loaded successfully!")
            print("----------------------------------------------------------------------------")

class Administrator:
    def __init__(self):
        self.library = Library()

    def add_book(self, book):
        self.library.add_book(book)
        
    def remove_book(self, book):
        if book in self.library.books:
            self.library.books.remove(book)
            print(f"Book: '{book.title}' is successfully removed from the library.")
            print("----------------------------------------------------------------------------")
        else:
            print(f"Book: '{book.title}' was not found in the library.")
            print("----------------------------------------------------------------------------")
    
    def add_patron(self, patron):
        self.library.add_patron(patron)

    def remove_patron(self, patron):
        if patron in self.library.patrons:
            self.library.patrons.remove(patron)
            print(f"Patron: '{patron.name}' is successfully removed from the library.")
            print("----------------------------------------------------------------------------")
        else:
            print(f"Patron: '{patron.name}' was not found in the library.")
            print("----------------------------------------------------------------------------")