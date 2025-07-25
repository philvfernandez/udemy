"""
Concerned with storing and retrieving books from a list.
"""

books = []

def add_book(name, author):
    books.append({'name': name, 'author': author, 'read': False})

def delete_book(name):
    for book in books:
        if book['name'] == name:
            books.remove(book)

def get_all_books():
    return books

def mark_book_as_read(name):
    for book in books:
        if book['name'] == name:
            book['read'] = True


## This works but is not a good idea to delete something from a lists while you are looping through the list.
##    for book in books:
##        if book['name'] == name:
##            book['read'] = True
##        else:
 ##           print('Book name Not Found.')


