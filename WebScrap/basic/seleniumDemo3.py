import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

browser = webdriver.Chrome("/Users/castlepan/chromedriver")
url = "http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable"
browser.get(url)
browser.switch_to.frame('iframeResult')
source = browser.find_element_by_css_selector('#droppable')
print(source)
try:
    logo = browser.find_element_by_css_selector('logo')
except NoSuchElementException:
    print('No LOGO')
    browser.switch_to.parent_frame()
    time.sleep(1)
    logo = browser.find_element_by_class_name('logo')
    print(logo)
    print(logo.text)
finally:
    browser.close()

