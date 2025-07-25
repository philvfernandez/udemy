"""
Concerned with storing and retrieving books from a list.
"""

books = []

def add_book(name, author):
    books.append({'name': name, 'author': author, 'read': False})

def delete_book(name):
    global books
    books = [book for book in books if book['name'] == name]

def list_books():
    global books
    for book in books:
        print(book)

def prompt_read_book(book_name):
    global books

    for book in books:
        if book['name'] == book_name:
            book['read'] = True
        else:
            print('Book name Not Found.')


