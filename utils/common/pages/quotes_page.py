from bs4 import BeautifulSoup

from utils.common.locators.quotes_page_locators import QuotesPageLocators
from utils.common.parsers.quote import QuoteParser

class QuotesPage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def quotes(self):
        locator = QuotesPageLocators.QUOTE
        quote_tags = self.soup.select(locator)
        return [QuoteParser(e) for e in quote_tags]