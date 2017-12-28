from selenium import webdriver
from pyquery import PyQuery as pq

driver = webdriver.PhantomJS()
driver.get("http://www.baidu.com")
# print(driver.page_source)

