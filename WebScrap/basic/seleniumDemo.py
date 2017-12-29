from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


browser = webdriver.Chrome("/Users/castlepan/chromedriver-Darwin")
# browser = webdriver.Safari()
try:
    browser.get('https://www.baidu.com')
    inputs = browser.find_element_by_id('kw')
    inputs.send_keys('Python')
    inputs.send_keys(Keys.ENTER)
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
    print(browser.current_url)
    print(browser.get_cookies())
    print(browser.page_source)
finally:
    browser.close()
