from selenium import webdriver
from utils.common.pages.quotes_page import QuotesPageSelenium

chrome = webdriver.Chrome()
chrome.get('https://quotes.toscrape.com/search.aspx')
page = QuotesPageSelenium(chrome)

author = input("Enter the author you'd like quotes from: ")
page.select_author(author)

tags = page.get_available_tags()
print("Select one of these tags: [{}]".format(' | '.join(tags))) # love | music | anything
selected_tag = input("Enter your tag:")
page.select_tag(selected_tag)

