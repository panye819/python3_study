import re

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

# findall搜索字符串，以列表形式返回全部能匹配的子串
html = re.sub('<a.*?>|</a>', '', html)
print("The type of html is : "+str(type(html)))
res2 = re.findall('<li.*?>(.*?)</li>', html, re.S)
if res2:
    print(type(res2))
    count = 0
    while count < len(res2):
        print(res2[count].strip())
        count += 1

print("--"*50)
