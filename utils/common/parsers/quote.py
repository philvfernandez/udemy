from utils.common.locators.quote_locators import QuoteLocators
from selenium.webdriver.common.by import By

class QuoteParser:
    """
    Given one of the specific quote divs, find out the data about the quote (quote, content, author, tags)
    """
    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'<Quote {self.content}, by {self.author}>'

    @property
    def content(self):
        locator = QuoteLocators.CONTENT
        return self.parent.select_one(locator).string

    @property
    def author(self):
        locator = QuoteLocators.AUTHOR
        return self.parent.select_one(locator).string

    @property
    def tags(self):
        locator = QuoteLocators.TAGS
        return [e.string for e in self.parent.select(locator)]

class QuoteSeleniumParser:
    """
    Given one of the specific quote divs, find out the data about the quote (quote, content, author, tags)
    """
    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f"<Quote {self.content}, by {self.author}>"

    @property
    def content(self):
        locator = QuoteLocators.CONTENT_LOCATOR
        return self.parent.find_element(By.CSS_SELECTOR, locator).text

    @property
    def author(self):
        locator = QuoteLocators.AUTHOR_LOCATOR
        return self.parent.find_element(By.CSS_SELECTOR, locator).text

    @property
    def tags(self):
        locator = QuoteLocators.TAGS_LOCATOR
        return self.parent.find_element(By.CSS_SELECTOR, locator).text

