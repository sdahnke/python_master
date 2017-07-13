import re

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
basket = []

rows = basket_table.find_all('tr')
# print(rows)
for row in rows:
    cells = row.find_all('td')
    #print(cells)
    if len(cells) > 0:
        position = cells[1].text.strip()
        print(position)
    #    attr1 = cells[2].text.strip()
    #    attr2 = cells[3].text.strip()
    #    attr3 = cells[4].text.strip()

    #    product_price = {position, attr1, attr2, attr3}
    #    basket.append(product_price)

print(basket)


# Warenkorb leeren
