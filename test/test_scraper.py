import requests
from bs4 import BeautifulSoup

url = requests.get("http://www.yellowpages.com/search?search_terms=coffee&geo_location_terms=Los+Angeles%2C+CA")

soup = BeautifulSoup(url.content, "html.parser")

# soup.find_all gibt eine Liste aller elemente aus!
# mit "for ELEMENT in LISTE:" kann man jedes einzelende Element durchgehen
links = soup.find_all("a")
for link in links:
    #print("<a href='%s'>%s</a>" %(link.get("href"),link.text))

# suche explizit in "div" die Klasse (class) "info"!!
g_data = soup.find_all("div", {"class": "info"})

for item in g_data:
    #print(item.contents[0].find_all(("a"), {"class": "business-name"}))