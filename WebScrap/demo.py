from selenium import webdriver
from pyquery import PyQuery as pq
import pymysql
import pymongo
import redis

# driver = webdriver.PhantomJS()
# driver.get("http://www.baidu.com")
# print(driver.page_source)


doc = pq('<html>hello</html>')
result = doc('html').text()
print(result)
print("-"*16)

conn = pymysql.connect(host='localhost', user='root', password='',
                       port=3306, db='mysql')
cursor = conn.cursor()
cursor.execute('select * from db')
print(cursor.fetchone())

print("-"*16)

client = pymongo.MongoClient('localhost')
db = client['newtestdb']
db['table'].insert({'name': 'Bob'})
print(db['table'].find_one({'name': 'Bob'}))

print("-"*16)

r = redis.Redis('localhost', 6379)
r.set('name', 'Bob')
print(r.get('name'))



