'''
Question-2: 
Nested Dictionaries You are managing a library. Here's the information about some books:

books = { 'book1': { 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'year': 1925 }, 
          'book2': { 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'year': 1960 }, 
          'book3': { 'title': '1984', 'author': 'George Orwell', 'year': 1949 } } 

a) Add a new book to the dictionary with the title, author, and year. 
b) Print the titles of all the books. 
c) Determine the book with the earliest publication year and print its title and author.
'''

books = { 'book1': { 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'year': 1925 }, 
          'book2': { 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'year': 1960 }, 
          'book3': { 'title': '1984', 'author': 'George Orwell', 'year': 1949 } }

#a)
new_book = {'title': 'The Godfather', 'author': 'Mario Puzo', 'year': 1969}
books['book4'] = new_book

#b)
print("Titles of all the books:")
print("1)", books['book1']['title'])
print("2)", books['book2']['title'])
print("3)", books['book3']['title'])
print("4)", books['book4']['title'])
print("----------------------------------")
#c)
earliest=books['book1']['year']
e_book='book1'
if earliest>books['book2']['year']:
    earliest=books['book2']['year']
    e_book='book2'
if earliest>books['book3']['year']:
    earliest=books['book3']['year']
    e_book='book3'
if earliest>books['book4']['year']:
    earliest=books['book4']['year']
    e_book='book4'
print("Book with earliest publication year:")
print("Title :", books[e_book]['title'])
print("Author :", books[e_book]['author'])
print("----------------------------------")