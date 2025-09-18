from selenium import webdriver
from utils.common.pages.quotes_page import QuotesPageSelenium
from utils.common.pages.quotes_page import QuotesPage

author = input("Enter the author you'd like quotes from: ")
tag = input("Enter your tag: ")

chrome = webdriver.Chrome()
chrome.get('https://quotes.toscrape.com/search.aspx')
page = QuotesPageSelenium(chrome)

#page.select_author(author)
#page.select_tag(selected_tag)
#page.search_button.click()

print(page.search_for_quotes(author, tag))