__author__ = 'steffendahnke'

import requests
from bs4 import BeautifulSoup
import re
from time import sleep
import csv
# regex -> result = re.match(pattern, string)

url = requests.get("https://www.hardpartsdirect.com/site-map")

soup = BeautifulSoup(url.content, "html.parser")

links = soup.find_all("a",  )

for link in links:
    # nur Links in der Kategorie Dirt-Bike (MX)
    if re.search("^.*http.*Products/Dirt-Bike.*$", str(link)):
        # zeige alle Produkt-Kategorie-Links
        # print(link.get('href'))

        url = requests.get(link.get('href'))
        soup = BeautifulSoup(url.content, "html.parser")
        links = soup.find_all("a", href=True)
        for link in links:
            if re.search("^.*action=ShowMeAllProducts.*$", str(link)):
                # zeigt alle Kategorie-URL mit Produkten :)
                kategorie_url = "https://www.hardpartsdirect.com/" + link.get('href')
                # print(kategorie_url)

                n = 0
                x = 0
                while 1 > x:

                    url = requests.get(kategorie_url + "&pageIndex=" + str(n))
                    soup = BeautifulSoup(url.content, "html.parser")
                    product_list = soup.find("ul", {"class": "product-list"})

                    if re.search(
                            ".*Wir konnten leider keine Produkte finden, die mit Ihren Suchkriterien übereinstimmen.*",
                            str(product_list)):
                        x = 1

                    # print(x, kategorie_url + "&pageIndex=" + str(n))

                    n = n + 1
                    sleep(20)

                    products = soup.find_all("ul", {"class": "product-list"})
                    for product in products:
                        # Produkt-Links auf Seiten finden
                        # print(product)
                        for product_url in product.find_all("a"):
                            if re.search("^((?!img).)*$", str(product_url)):
                                every_product = "https://www.hardpartsdirect.com" + product_url.get("href")


                                print(every_product)

                                # Produkt öffnen
                                url = requests.get(every_product)
                                soup = BeautifulSoup(url.content, "html.parser")
                                #print(soup.prettify())

                                #Produktdetails extrahieren :)
                                sku = soup.find("h3", {"class" : "product-detail-product-number-heading"}).string
                                #print(sku)
                                name = soup.find("div", {"class" : "information"}).find("h1").string
                                print(name)
                                preis = soup.find("span", {"class" : "price"}).string
                                #print(preis)
                                pic_url = soup.find("div", {"class" : "preview"}).find(id="product-image").get("src")
                                #print(pic_url)
                                beschreibung = soup.find("p")
                                #print(beschreibung)
                                anwendungen = soup.find("div", {"class" : "detail"}).find("ul")
                                for anwendung in soup.find("div", {"class" : "detail"}).find("ul"):
                                    #print(anwendung.string)
                                    with open('hardpartsdirect.csv', 'a', newline='') as csvfile:
                                        writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)
                                        writer.writerow([sku, name, preis, anwendung.string, beschreibung, pic_url])

                                sleep(15)