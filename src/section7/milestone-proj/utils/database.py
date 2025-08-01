import json
import sqlite3

def create_book_table():
    connection = sqlite3.connect('data.db')
    # All operations in SQLite are made by cursors, and not by the connection object itself.
    # That is so that we can have one single connection, but potentially multiple cursors either reading data and
    # at most one writing data
    cursor = connection.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key , author text, read integer)')
    # Commit means save the result of this query to disk.
    # Keep a bunch of data in memory until we commit.
    # We can write multiple things together, which is faster.
    connection.commit()
    connection.close()


def add_book(name, author):
    connection = sqlite3.connect('data.db')
    # All operations in SQLite are made by cursors, and not by the connection object itself.
    # That is so that we can have one single connection, but potentially multiple cursors either reading data and
    # at most one writing data
    cursor = connection.cursor()

    cursor.execute('INSERT INTO books VALUES (?, ?, ?)', (name, author, 0))

    # Second query that can be used instead of above sql query.
    # Note: This is not recommended approach.
    # f'INSERT INTO books VALUES("{name", "{author}", 0)')

    # Commit means save the result of this query to disk.
    # Keep a bunch of data in memory until we commit.
    # We can write multiple things together, which is faster.
    connection.commit()
    connection.close()

def get_all_books():
    connection = sqlite3.connect('data.db')
    # All operations in SQLite are made by cursors, and not by the connection object itself.
    # That is so that we can have one single connection, but potentially multiple cursors either reading data and
    # at most one writing data
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM books')

    # list of tuples --> [(name, author, read), (name, author, read)...]
    # But to be consistent with our data structures, we will convert to list dictionaries as a comprehension
    books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]

    connection.close()
    return books

def mark_book_as_read(name):
    connection = sqlite3.connect('data.db')
    # All operations in SQLite are made by cursors, and not by the connection object itself.
    # That is so that we can have one single connection, but potentially multiple cursors either reading data and
    # at most one writing data
    cursor = connection.cursor()
    cursor.execute('UPDATE books SET read = ? WHERE name = ?', (1, name))
    connection.commit()
    connection.close()

def delete_book(name):
    connection = sqlite3.connect('data.db')
    # All operations in SQLite are made by cursors, and not by the connection object itself.
    # That is so that we can have one single connection, but potentially multiple cursors either reading data and
    # at most one writing data
    cursor = connection.cursor()

    cursor.execute('DELETE FROM books WHERE name = ?', (name,))
    connection.commit()
    connection.close()


