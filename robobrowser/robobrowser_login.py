import re
from robobrowser import RoboBrowser
from bs4 import BeautifulSoup

url = "https://mike.matthies.de"

br = RoboBrowser(history=True)
br.open(url)

form = br.get_form(id='quicklogin')

form["mcustno"] = "658073000"
form["mpassword"] = "online24"

# print(form)

br.session.headers["Referer"] = url

br.submit_form(form)

soup = BeautifulSoup(str(br.select), "html.parser")

category_links = soup.find_all('href')

for category_link in category_links:
    print(category_link)

