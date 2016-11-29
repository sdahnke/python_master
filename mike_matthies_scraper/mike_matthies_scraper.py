import re
from robobrowser import RoboBrowser
from bs4 import BeautifulSoup
import time

url = "https://mike.matthies.de"

br = RoboBrowser(history=True)

login_name = "658073000"
login_pw = "online24"

n = 0

category_list = list()
category_list_t = list()
every_prod_site = list()
prod_link_list = list()

# Login-Funktion implementieren
def matthieslogin(url):
    br.open(url)
    form = br.get_form(id='quicklogin')
    form["mcustno"] = login_name
    form["mpassword"] = login_pw
    # Formular ausgeben
    # print(form)
    br.session.headers["Referer"] = url
    br.submit_form(form)

matthieslogin(url)

soup = BeautifulSoup(str(br.select), "html.parser")

category_links = soup.find_all('a', href=True)

# sammle Kategorie-Links
for category_link in category_links:
    if re.search(".*category.*",str(category_link)):
        # print(str(category_link['href']))
        category_list.append(str(category_link['href']))

        # öffne Kategorie-Links mit Login!
        br.open(str(category_link['href']))
        soup = BeautifulSoup(str(br.select), "html.parser")
        site_links = soup.find_all('a')
        category_list_t = [0]
        for site_link in site_links:
            if re.search(".*sr=.*", str(site_link)):
                # print(site_link['href'])
                number_str = re.match(r".*sr=(.*)",str(site_link['href']))
                category_list_t.append(int(number_str.group(1)))

        # int(max(category_list_t))
        print(int(max(category_list_t)))

        n = 0

        while (n <= int(max(category_list_t))):
            # set site_url
            every_site = str(category_link['href']) + "?sr=" + str(n)
            every_prod_site.append(every_site)
            # n + 180
            n = n + 180

for prod_site in every_prod_site:
    # print(prod_site)
    br.open(str(prod_site))
    time.sleep(1)
    soup = BeautifulSoup(str(br.select), "html.parser")
    prod_links = soup.find_all('a')
    for prod_link in prod_links:
        if re.match(".*article.*",str(prod_link)):
            prod_link_list.append(prod_link['href'])
            print(prod_link['href'])

prod_link_list = list(set(prod_link_list))


print(len(prod_link_list))

