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

rows = basket_table.find_all('tr')
# print(rows)
for row in rows:
    cols = row.find_all('td')
    for ele in cols:
        cols = ele.text.strip()
        if re.match("([0-9]{3}).([0-9]{2}).([0-9]{2})#w1wkg", str(cols)):
            search = re.search("([0-9]{3}).([0-9]{2}).([0-9]{2})#w1wkg", cols)
            cols = search.group(1) + "." + search.group(2) + "." + search.group(3)
            print(cols)
        if re.match("[^0-9]+([0-9,]+)", str(cols)):
            search = re.search("[^0-9]+([0-9,]+)", cols)
            cols = search.group(1)
            print(cols)
        new_row = [ele for ele in cols if ele]
        if re.match("\[\'[0-9]+\'.*", str(new_row)):
            data.append(new_row)
            print(data)


# Warenkorb leeren
