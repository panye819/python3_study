import re
import requests


# 爬取豆瓣图书列表

content = requests.get('http://book.douban.com/').text
with open('book.txt', 'w+') as f:
    f.write(content)
    f.close()

# print(content)
# pattern = re.compile(
#     '<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">\
#     (.*?)</span>.*?year">(.*?)</span>.*?</li>', re.S)
#
# results = re.findall(pattern, content)
# # print(results)
# for result in results:
#     url, name, author, date = result
#     author = re.sub('\s', '', author)
#     date = re.sub('\s', '', date)
#     print(url, name, author, date)
#
