import re

content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
res = re.match('Hello.*?(\d+).*?Demo', content)
print(res)
print("--"*50)

# re.search 会扫描整个字符串并返回第一个成功的匹配
# res1 = re.search(content, 'Hello.*?(\d+).*?Demo')

res1 = re.search('Hello.*?(\d+).*?Demo', content)
print(res1)
print("--"*50)

html = """<div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
        经典老歌列表
    </p>
    <ul id="list" class="list-gtoup">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a> </li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a> </li>
        <li data-view="5">
            <a href="/6.mp3" singer="郑丽君"><i class="fa fa-user"></i>往事随风</a>
        </li>
    </ul>
</div>
"""
res2 = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>', html, re.S)
if res2:
    print(res2.group(1), res2.group(2))

print("--"*50)
res3 = re.search('<li.*?singer="(.*?)">(.*?)</a>', html, re.S)
if res3:
    print(res3.group(1), res3.group(2))

print("--"*50)
res4 = re.search('<li.*?singer="(.*?)">(.*?)</a>', html)
if res4:
    print(res4.group(1), res4.group(2))
