import json
import sqlite3

"""
Concerned with storing and retrieving books from a json file.
Format of the JSON file

[
    {
        'name': 'Clean Code',
        'author': 'Robert'
        'read': True
    }
]
...
"""

books_file = 'books.json'


def create_book_table():
    connection = sqlite3.connect('data.db')
    # All operations in SQLite are made by cursors, and not by the connection object itself.
    # That is so that we can have one single connection, but potentially multiple cursors either reading data and
    # at most one writing data
    cursor = connection.cursor()

    cursor.execute('CREATE TABLE books(name text primary key , author text, read integer)')
    # Commit means save the result of this query to disk.
    # Keep a bunch of data in memory until we commit.
    # We can write multiple things together, which is faster.
    connection.commit()
    connection.close()


def add_book(name, author):
    books = get_all_books()
    books.append({'name': name, 'author': author, 'read': False})
    _save_all_books(books)

def get_all_books():
    with open(books_file, 'r') as file:
        return json.load(file) ## Returns a list

def _save_all_books(books): # no private method in python so the convention is to prepend the method with a '_'.
    with open(books_file, 'w') as file:
        json.dump(books, file)

def mark_book_as_read(name):
    books = get_all_books()

    for book in books:
        if book['name'] == name:
            book['read'] = True

    _save_all_books(books)

def delete_book(name):
    books = get_all_books()

    books = [book for book in books if book['name'] != name]
    _save_all_books(books)

## This works but is not a good idea to delete something from a lists while you are looping through the list.
##    for book in books:
##        if book['name'] == name:
##            book['read'] = True
##        else:
 ##           print('Book name Not Found.')


