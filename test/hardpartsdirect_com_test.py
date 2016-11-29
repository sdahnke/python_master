import requests
from bs4 import BeautifulSoup

url = requests.get("https://www.hardpartsdirect.com/Products/Dirt-Bike")

soup = BeautifulSoup(url.content, "html.parser")

print(soup.prettify())