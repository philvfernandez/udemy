from selenium import webdriver
from utils.common.pages.quotes_page import QuotesPageSelenium

chrome = webdriver.Chrome()
chrome.get('https://quotes.toscrape.com/search.aspx')
page = QuotesPageSelenium(chrome)

for quote in page.quotespageselenium:
    print(quote)