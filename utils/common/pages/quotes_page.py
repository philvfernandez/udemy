from typing import List

from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select

from src.section2.s02_l29_for_loops import element
from utils.common.locators.quotes_page_locators import QuotesPageLocators
from utils.common.parsers.quote import QuoteParser, QuoteSeleniumParser
from selenium.webdriver.common.by import By


class QuotesPage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def quotes(self):
        locator = QuotesPageLocators.QUOTE
        quote_tags = self.soup.select(locator)
        return [QuoteParser(e) for e in quote_tags]

class QuotesPageSelenium:
    def __init__(self, browser):
        self.browser = browser

    @property
    def quotespageselenium(self) -> List[QuoteSeleniumParser]:
        return [
            QuoteSeleniumParser(e) for e in self.browser.find_elements(By.CSS_SELECTOR, QuotesPageLocators.QUOTE)
        ]

    @property
    def author_dropdown(self) -> Select:
        element = self.browser.find_element(By.CSS_SELECTOR, QuotesPageLocators.AUTHOR_DROPDOWN)
        return Select(element)

    def select_author(self, author_name: str):
        self.author_dropdown.select_by_visible_text(author_name)

    @property
    def tags_dropdown(self) -> Select:
        element = self.browser.find_element(By.CSS_SELECTOR, QuotesPageLocators.TAGS_DROPDOWN)
        return Select(element)

    def get_available_tags(self) -> List[str]:
        return[option.text.strip() for option in self.tags_dropdown.options]

    def select_tag(self, tag_name: str):
        self.tags_dropdown.select_by_visible_text(tag_name)
