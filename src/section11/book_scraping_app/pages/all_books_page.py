import re
import logging
from bs4 import BeautifulSoup

from src.section11.book_scraping_app.locators.all_books_page import AllBooksPageLocators
from src.section11.book_scraping_app.parsers.book_parser import BookParser

logger = logging.getLogger('scraping.all_books_page') # Gives a child logger of the main logger scrapping

class AllBooksPage:
    def __init__(self, page_content):
        logger.debug('Parsing page content with BeautifulSoup HTML parser.')
        self.soup = BeautifulSoup(page_content, 'html.parser')

    @property
    def books(self):
        logger.debug(f'Finding all books in the page using `{AllBooksPageLocators.BOOKS}` CSS selector.')
        return [BookParser(e) for e in self.soup.select(AllBooksPageLocators.BOOKS)]

    @property
    def page_count(self):
        logger.debug('Finding all number of catalogue pages available from book scraping website...')
        content = self.soup.select_one(AllBooksPageLocators.PAGER).string
        logger.info(f'Found number of catalogue pages: {content}')
        pattern = 'Page [0-9]+ of ([0-9]+)'
        matcher = re.search(pattern, content)
        pages = int(matcher.group(1))
        logger.debug(f'Extracted number of pages: {pages}')
        return pages
