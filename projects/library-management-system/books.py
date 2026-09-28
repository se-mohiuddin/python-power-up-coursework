#books
class Book:
    def __init__(self, title="", author="", ISBN=0, total_copies=0):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.total_copies = total_copies
        self.available_copies = total_copies