from bs4 import BeautifulSoup
from robobrowser import RoboBrowser

url = "https://www.ebay-kleinanzeigen.de/p-anzeige-aufgeben.html#?path=210/306/teile&isParent=false"

br = RoboBrowser(history=False)

login_name = "steffen_info@hotmail.com"
login_pw = "online24"


# Login-Funktion implementieren
def ebay_k(url):
    br.open(url)
    form = br.get_form(id='login-form')
    form["loginMail"] = login_name
    form["password"] = login_pw
    br.session.headers["Referer"] = url
    br.submit_form(form)


ebay_k(url)
form = br.get_form(id="postad-step1-frm")
br.submit_form(form)

soup = BeautifulSoup(str(br.select), "lxml")

print(soup.prettify())
