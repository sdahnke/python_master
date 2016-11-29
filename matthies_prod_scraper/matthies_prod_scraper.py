import re
from robobrowser import RoboBrowser
from bs4 import BeautifulSoup
import time
import csv


url = "http://mike.matthies.de/de/category/10410400000/article/364601/"

br = RoboBrowser(history=True)

login_name = "658073000"
login_pw = "online24"

n = 0
cat_list = list()
bez_list = list()
pic_list = list()
car_list = list()

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
#print(soup.prettify())

id_prod = soup.find('div', {'class':'tooltips_text breit150'})
id_prod = id_prod.text
print(id_prod)

categorie = soup.find('ul', {'id':'details_productebenen'})
for cat in categorie.find_all('li'):
    cat_list.append(cat.text)
print(cat_list)

verfügbar = soup.find('div', {'class':'avail_wrap'})
verfügbar = verfügbar.text
print(verfügbar)

beschreibung = soup.find('div', {'class':'tab_container'})
if re.match('.*Beschreibung.*', str(beschreibung)):
    beschreibung = beschreibung.text
    print(beschreibung)

bezeichnungen = soup.find_all('div', {'class':'mm_drow'})
for bezeichnung in bezeichnungen:
    bez_list.append(bezeichnung.text)
print(bez_list)

pics_url = soup.find('div', {'class':'mm_images_box'})
pics_url = pics_url.find_all('a')
for pic_url in pics_url:
    pic_list.append(pic_url['href'])
print(pic_list)

mobile_table = soup.find_all('div', {'class':'title'})
for fahrzeug in mobile_table:
    if re.match('.*table.*', str(fahrzeug)):
        car_list.append(fahrzeug.text)
print(car_list)


with open('matthies_prod.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)
    writer.writerow([id_prod, cat_list, verfügbar, beschreibung, bez_list, pic_list, car_list])

cat_list.clear()
bez_list.clear()
pic_list.clear()
car_list.clear()

time.sleep(2)




