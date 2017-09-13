from pywinauto import findwindows
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

driver.find_element_by_id('pictureupload-pickfiles').click()

##app = Application().Start(cmd_line=u'"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe" --disable-background-networking --disable-client-side-phishing-detection --disable-default-apps --disable-hang-monitor --disable-popup-blocking --disable-prompt-on-repost --disable-sync --disable-web-resources --enable-automation --enable-logging --force-fieldtrials=SiteIsolationExtensions\\Control --ignore-certificate-errors --load-component-extension="C:\\Users\\sdahnke\\AppData\\Local\\Temp\\scoped_dir5040_24469\\internal" --log-level=0 --metrics-recording-only --no-first-run --password-store=basic --remote-debugging-port=12007 --safebrowsing-disable-auto-update --test-type=webdriver --use-mock-keychain --user-data-dir="C:\\Users\\sdahnke\\AppData\\Local\\Temp\\scoped_dir5040_31373" data:,')

app = findwindows.find_window(title_re=u'.*ffnen.*', class_name='Window')
window = app.Dialog
window.Wait('ready')
toolbar = window.Toolbar3
toolbar.Click()
toolbar.Edit.type_keys("pywinauto Works!")
