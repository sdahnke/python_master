import re
from robobrowser import RoboBrowser
from bs4 import BeautifulSoup
import time
import csv
import os.path

url = "http://mike.matthies.de/de/category/10410000000/"

br = RoboBrowser(history=False)

login_name = "658073000"
login_pw = "online24"

n = 0

category_list = list()
category_list_t = list()
every_prod_site = list()
prod_link_list = list()

cat_list = list()
bez_list = list()
pic_list = list()
car_list = list()

csv_name = 'matthies_prod_zylinder' + '.csv'

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

# -------------------------------------------------------------------------------------------------------------

matthieslogin(url)

soup = BeautifulSoup(str(br.select), "html.parser")

category_links = soup.find_all('a', href=True)

# sammle Kategorie-Links
for category_link in category_links:
    if re.search(".*ccm.*", str(category_link)):
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
                number_str = re.match(r".*sr=(.*)", str(site_link['href']))
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

if os.path.isfile('temp_file.csv'):
    # do not search new 'prod_links' and begin to read 'temp_file.csv'
    pass
else:
    for prod_site in every_prod_site:
        # print(prod_site)
        br.open(str(prod_site))
        time.sleep(2)
        soup = BeautifulSoup(str(br.select), "html.parser")
        prod_links = soup.find_all('a')
        for prod_link in prod_links:
            # find only Links (href) in images (img)
            if re.match(".*article.*", str(prod_link)):
                # print(prod_link)
                # write data to file (tmp_file)
                with open('temp_file.csv', 'a', newline='') as csvfile:
                    temp_writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)
                    temp_writer.writerow([prod_link['href']])

                # print(str(prod_link['href']))

category_list.clear()
category_list_t.clear()
every_prod_site.clear()
prod_link_list.clear()

# -------------------------------------------------------------------------------------------------------------

# read lines from temp_file
with open('temp_file.csv', newline='') as csvfile:
    temp_reader = csv.reader(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)
    for prod_link in temp_reader:
        try:
            url_string = re.findall(".*(http.*)'.*",str(prod_link))
            br.open(url_string[0])
            soup = BeautifulSoup(str(br.select), "html.parser")
            # print(soup.prettify())
        except:
            print('cant open link ' + url_string[0])

        try:
            id_prod = soup.find('div', {'class': 'tooltips_text breit150'})
            id_prod = id_prod.text
            print(str(id_prod))
        except:
            id_prod = '#no id_prod'

        try:
            categorie = soup.find('ul', {'id':'details_productebenen'})
            for cat in categorie.find_all('li'):
                cat_list.append(cat.text)
            # print(cat_list)
        except:
            cat_list.append('#no cat_list')

        try:
            verfügbar = soup.find('div', {'class': 'avail_wrap'})
            verfügbar = verfügbar.text
            # print(verfügbar)
        except:
            verfügbar = '#no verfügbar'

        try:
            beschreibung = soup.find('div', {'class': 'tab_container'})
            if re.match('.*Beschreibung.*', str(beschreibung)):
                beschreibung = beschreibung.text
                # print(beschreibung)
        except:
            beschreibung = '#no beschreibung'

        try:
            bezeichnungen = soup.find_all('div', {'class': 'mm_drow'})
            for bezeichnung in bezeichnungen:
                bez_list.append(bezeichnung.text)
            # print(bez_list)
        except:
            bez_list.append('#no bezeichnung')

        try:
            pics_url = soup.find('div', {'class': 'mm_images_box'})
            pics_url = pics_url.find_all('a')
            for pic_url in pics_url:
                pic_list.append(pic_url['href'])
            # print(pic_list)
        except:
            pic_list.append('#no pic_list')

        try:
            mobile_table = soup.find_all('div', {'class': 'title'})
            for fahrzeug in mobile_table:
                if re.match('.*table.*', str(fahrzeug)):
                    car_list.append(fahrzeug.text)
            # print(car_list)
        except:
            mobile_table.append('#no mobile_table')

        with open(str(csv_name), 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)
            writer.writerow([url_string[0], id_prod, cat_list, verfügbar, beschreibung, bez_list, pic_list, car_list])

        cat_list.clear()
        bez_list.clear()
        pic_list.clear()
        car_list.clear()

        time.sleep(2)