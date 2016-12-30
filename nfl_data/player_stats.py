from robobrowser.browser import RoboBrowser
from bs4 import BeautifulSoup
import re

player_links = []
letter_list = []

url = "http://www.footballdb.com/players/players.html?letter=A"

br = RoboBrowser(history=False)

def player(url):
    br.open(url)
    soup = BeautifulSoup(str(br.select), "html.parser")
    table = soup.find('table', attrs={'class':'statistics'})
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')

    for row in rows:
        link = row.find('a', href=True)
        link = link['href']
        player_links.append(link)

# catch A side player
player(url)

# catch all other letter
br.open(url)
soup = BeautifulSoup(str(br.select), "html.parser")

link_list = soup.find_all('a', href=True)

for link in link_list:
    if re.search(".*letter=.*", str(link)):
        letter_list.append(str(link['href']))

for letter in letter_list:
    letter_url = 'http://www.footballdb.com' + letter
    player(letter_url)

print(player_links)

print(len(player_links))

for player_link in player_links:
    player_url = 'http://www.footballdb.com' + player_link + '/stats'
    br.open(player_url)
    soup = BeautifulSoup(str(br.select), "html.parser")
