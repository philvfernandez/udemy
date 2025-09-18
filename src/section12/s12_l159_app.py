from selenium import webdriver
from utils.common.pages.quotes_page import QuotesPageSelenium, InvalidTagForAuthorError
from utils.common.pages.quotes_page import QuotesPage

try:

    author = input("Enter the author you'd like quotes from: ")
    tag = input("Enter your tag: ")

    chrome = webdriver.Chrome()
    chrome.get('https://quotes.toscrape.com/search.aspx')
    page = QuotesPageSelenium(chrome)

    #page.select_author(author)
    #page.select_tag(selected_tag)
    #page.search_button.click()

    print(page.search_for_quotes(author, tag))

except InvalidTagForAuthorError as e:
    print(e)
except Exception as e:
    print(e)
    print("An Unknown error occurred.  Please try again.")
finally:
    chrome.quit()