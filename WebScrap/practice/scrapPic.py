import time
from selenium import webdriver


browser = webdriver.Chrome("/Users/castlepan/chromedriver")
url1 = "https://www.baidu.com"
url2 = "https://www.taobao.com"
url3 = "https://mail.163.com"

browser.get(url1)
browser.execute_script('window.open()')
print(browser.window_handles)
time.sleep(1)
browser.switch_to.window(browser.window_handles[1])
browser.get(url2)
time.sleep(1)
browser.execute_script('window.open()')
time.sleep(1)
browser.switch_to.window(browser.window_handles[2])
browser.get(url3)
# browser.back()
# time.sleep(1)
# browser.forward()
browser.close()
browser.switch_to.window(browser.window_handles[1])
browser.close()
browser.switch_to.window(browser.window_handles[0])
browser.close()
