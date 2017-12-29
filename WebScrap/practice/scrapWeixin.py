import requests
import time
import os
import pymongo
from pyquery import PyQuery as pq
from urllib.parse import urlencode
from requests.exceptions import ConnectionError

base_url = 'http://weixin.sogou.com/weixin?'
client = pymongo.MongoClient('localhost')
db = client['weixin']
headers = {
    'Cookie': 'ABTEST=0|1514527483|v1; IPLOC=CN3201; SUID=526AD53A2930990A000000005A45DAFB; SUID=526AD53A6119940A000000005A45DAFB; weixinIndexVisited=1; SUV=00E75AA03AD56A525A45DAFBD1B99609; SNUID=A9912FC0FBFF9B8E8D4431BCFBF5C85A; JSESSIONID=aaaBtwV5fgQ888x_A_v8v; sct=5',
    'Host': 'weixin.sogou.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36 OPR/49.0.2725.64'
}
keyword = 'DevOps'


def get_html(url):
    try:
        response = requests.get(url, allow_redirects=False)
        if response.status_code == 200:
            return response.text
        if response.status_code == 302:
            # need proxy
            # pass
            print("302 appear ! You need a proxy!!!")
    except ConnectionError:
        return get_html(url)


def get_index(keyword, page):
    data = {
        'query': keyword,
        'type': 2,
        'page': page
    }
    queries = urlencode(data)
    url = base_url+queries
    html = get_html(url)
    return html


def parse_index(html):
    doc = pq(html)
    items = doc('.news-box .news-list li .txt-box h3 a').items()
    for item in items:
        yield item.attr('href')


def get_detail(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError:
        return None


def parse_detail(html):
    doc = pq(html)
    title = doc('.rich_media_title').text()
    content = doc('.rich_media_content').text()
    date = doc('#post-date').text()
    nickname = doc('#js_profile_qrcode > div > strong').text()
    wechat = doc('#post-user').text()
    return {
        'title': title,
        'content': content,
        'date': date,
        'nickname': nickname,
        'wechat': wechat
    }


def save_to_mongo(data):
    if db['articles'].update({'title': data['title']}, {'$set': data}, True):
        print("Saved to Mongo Succed!", data['title'])
    else:
        print("Saved to Mongo Failed!", data['title'])


def main():
    for page in range(1, 11):
        print("开始爬取 " + str(page)+" 页的文章。。。")
        html = get_index(keyword, page)
        if html:
            article_urls = parse_index(html)
            for article_url in article_urls:
                # print(article_url)
                # os.system('scrapy view ')
                article_html = get_detail(article_url)
                if article_html:
                    article_data = parse_detail(article_html)
                    print(article_data)
                    save_to_mongo(article_data)
        time.sleep(5)


if __name__ == '__main__':
    main()
