import time

import pywinauto
from splinter import Browser

url = "https://www.ebay-kleinanzeigen.de/p-anzeige-aufgeben.html#?path=210/306/teile&isParent=false"
login_name = "steffen_info@hotmail.com"
login_pw = "online24"

browser = Browser('chrome')
browser.driver.set_window_size(1400, 1000)
browser.visit(url)

browser.fill('loginMail', login_name)
browser.fill('password', login_pw)
browser.click_link_by_id("login-submit")

browser.find_by_id("cat_210").click()
browser.find_by_id("cat_306").click()
browser.find_by_id("cat_teile").click()
browser.find_by_css('.button').first.click()

browser.fill('title', 'Titel der Anzeige')
browser.fill('description', 'Anzeigentext')
browser.fill('priceAmount', '100')
browser.find_by_id("priceType2").click()

browser.find_by_id('pictureupload-pickfiles').click()
time.sleep(5)
apps = pywinauto.findwindows.find_elements(title_re='Öffnen')
for app in apps:
    print(app)


    # window = app.Dialog
    # window.Wait('ready')
    # edit = window.Edit
    # edit.RightClickInput()
    # edit.Select()
    # edit.ClickInput()
    # button = window.Button
    # button.Click()
