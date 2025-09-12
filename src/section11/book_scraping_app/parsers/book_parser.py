import re
import logging

from bs4 import BeautifulSoup

from src.section11.book_scraping_app.locators.book_locators import BookLocators
from src.section11.s11_l154_class_html_parsing import ParsedItemLocators

logger = logging.getLogger('scraping.book_parser')

class BookParser:

    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5,
    }

    def __init__(self, parent):
        logger.debug(f'New book parser created from {parent}.') # prints out entire HTML
        self.parent = parent

    def __repr__(self):
        return f'<Book: {self.name}, £{self.price}, {self.rating} stars>'


    @property
    def name(self):
        logger.debug('Finding book name...')
        locator = BookLocators.NAME_LOCATOR
        item_link = self.parent.select_one(locator)
        item_name = item_link.attrs['title']
        logger.debug(f'Found book name: {item_name}.')
        return item_name

    @property
    def link(self):
        logger.debug('Finding book link...')
        locator = BookLocators.LINK_LOCATOR
        item_link = self.parent.select_one(locator).attrs['href']
        logger.debug(f'Found book link: {item_link}.')
        return item_link

    @property
    def price(self):
        logger.debug('Finding book price...')
        locator = BookLocators.PRICE_LOCATOR
        item_price = self.parent.select_one(locator).string # £51.77

        pattern = '£([0-9]+\.[0-9]+)'
        matcher = re.search(pattern, item_price)
        logger.debug(f'Found book price: {matcher.group(1)}.')
        return float(matcher.group(1))

    @property
    def rating(self):
        logger.debug('Finding book rating...')
        locator = BookLocators.RATING_LOCATOR
        star_rating_tag = self.parent.select_one(locator)
        classes = star_rating_tag.attrs['class'] # ['star-rating', 'Three']
        rating_classes = [r for r in classes if r != 'star-rating']
        rating_number = BookParser.RATINGS.get(rating_classes[0]) # None if not found
        logger.debug(f'Found book rating: {rating_number}.')
        return rating_number