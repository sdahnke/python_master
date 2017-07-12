import csv
import re
import time
from bs4 import BeautifulSoup
from robobrowser import RoboBrowser

url = "https://www.matthies.de/warenkorb/warenkorb.html?no_cache=1"

br = RoboBrowser(history=False)

login_name = "658073000"
login_pw = "online24"

br.open(url)
forms = br.get_forms()
for form in forms:
    form["user"] = login_name
    form["pass"] = login_pw
    br.submit_form(form)

soup = BeautifulSoup(str(br.select), "lxml")

basket_table = soup.find('table', attrs={'class':'tx_nbbasket'})
# basket_body = basket_table.find('tbody')
# print(basket_body)

data = []

rows = basket_table.find_all('tr')
#print(rows)
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    if re.match("716\u200977\u200994#w1wkg", cols):
        print("convert to matthies_id")
    if re.match("€\xa020,00", cols):
        print("convert to number")

    new_row = [ele for ele in cols if ele]
    if re.match("\[\'[0-9]+\'.*", str(new_row)):
        print(new_row)
        data.append(new_row)

# Warenkorb leeren
