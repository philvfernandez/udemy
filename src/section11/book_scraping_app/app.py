import requests

from src.section11.book_scraping_app.pages.all_books_page import AllBooksPage

page_content = requests.get('https://books.toscrape.com').content
page = AllBooksPage(page_content)

books = page.books

for book in books:
    print(book)