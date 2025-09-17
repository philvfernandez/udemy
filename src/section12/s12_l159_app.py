from selenium import webdriver
from utils.common.pages.quotes_page import QuotesPageSelenium

chrome = webdriver.Chrome()
chrome.get('https://quotes.toscrape.com/search.aspx')
page = QuotesPageSelenium(chrome)

author = input("Enter the author you'd like quotes from: ")
page.select_author(author)
