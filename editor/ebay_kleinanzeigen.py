from selenium import webdriver

url = "https://www.ebay-kleinanzeigen.de/p-anzeige-aufgeben.html#?path=210/306/teile&isParent=false"
login_name = "steffen_info@hotmail.com"
login_pw = "online24"

driver = webdriver.Chrome(executable_path='D:\chromedriver\chromedriver.exe')
driver.get(url)
driver.find_element_by_id("login-email").send_keys(login_name)
driver.find_element_by_id("login-password").send_keys(login_pw)

driver.find_element_by_id("login-submit").click()

driver.find_element_by_id("cat_210").click()
driver.find_element_by_id("cat_306").click()
driver.find_element_by_id("cat_teile").click()
driver.find_element_by_class_name("button").click()

driver.find_element_by_id("postad-title").send_keys("Titel der Anzeige")
driver.find_element_by_id("pstad-descrptn").send_keys("Anzeigentext")
driver.find_element_by_id("pstad-price").send_keys("100")
driver.find_element_by_id("priceType2").click()

driver.find_element_by_id("pictureupload-pickfiles").click()
