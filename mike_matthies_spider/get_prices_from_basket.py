import re

from bs4 import BeautifulSoup
from robobrowser import RoboBrowser

url = "https://www.matthies.de/warenkorb/warenkorb.html?no_cache=1"

br = RoboBrowser(history=False)

login_name = "658073000"
login_pw = "online24"

basket = []
basket_products = []

br.open(url)
forms = br.get_forms()
for form in forms:
    form["user"] = login_name
    form["pass"] = login_pw
    br.submit_form(form)

soup = BeautifulSoup(str(br.select), "lxml")

basket_table = soup.find('table', attrs={'class':'tx_nbbasket'})

rows = basket_table.find_all('tr')
for row in rows:
    cells = row.find_all('td')
    for cell in cells:
        cell = str(cell.text.strip())
        if re.match("([0-9]{3}).([0-9]{2}).([0-9]{2})#w1wkg", cell):
            search = re.search("([0-9]{3}).([0-9]{2}).([0-9]{2})#w1wkg", cell)
            cell = search.group(1) + "." + search.group(2) + "." + search.group(3)
        if re.match("[^0-9]+([0-9,]+)", cell):
            search = re.search("[^0-9]+([0-9,]+)", cell)
            cell = search.group(1)
        basket_products.append(cell)
    if re.match("\[\'[0-9]+\',.*", str(basket_products)):
        print(str(basket_products))
        basket.append(basket)
    basket_products = []

print(basket)


# Warenkorb leeren
