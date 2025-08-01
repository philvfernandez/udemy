from .database_connection import DatabaseConnection

def create_book_table():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key , author text, read integer)')


def add_book(name, author):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('INSERT INTO books VALUES (?, ?, ?)', (name, author, 0))


def get_all_books():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM books')

        # list of tuples --> [(name, author, read), (name, author, read)...]
        # But to be consistent with our data structures, we will convert to list dictionaries as a comprehension
        books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]

    return books

def mark_book_as_read(name):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        # All operations in SQLite are made by cursors, and not by the connection object itself.
        # That is so that we can have one single connection, but potentially multiple cursors either reading data and
        # at most one writing data
        cursor = connection.cursor()
        cursor.execute('UPDATE books SET read = ? WHERE name = ?', (1, name))

def delete_book(name):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        # All operations in SQLite are made by cursors, and not by the connection object itself.
        # That is so that we can have one single connection, but potentially multiple cursors either reading data and
        # at most one writing data
        cursor = connection.cursor()
        cursor.execute('DELETE FROM books WHERE name = ?', (name,))


