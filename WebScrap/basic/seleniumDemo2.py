from selenium import webdriver


browser = webdriver.Chrome("/Users/castlepan/chromedriver")

browser.get('https://www.zhihu.com/explore')
inputs = browser.find_element_by_class_name('zu-top-add-question')
print(inputs.text)
print(inputs.id)
print(inputs.location)
print(inputs.tag_name)
print(inputs.size)

browser.close()

