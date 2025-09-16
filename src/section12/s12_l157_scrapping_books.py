import requests
from bs4 import BeautifulSoup

URL = 'https://example.com/'
page = requests.get(URL)
# print(page.content)
soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.prettify())
print(soup.find('h1').string)
print(soup.select_one('p a').attrs['href'])