from pyquery import PyQuery as pq

html = """
<div id="container">
    <ul class="list">
     <li class="item-0">first item</li>
     <li class="item-1"><a href="link2.html"></a>second item</li>
     <li class="item-0 active"><a>href="link3.html"</a><span class="bold"></span>third item</li>
     <li class="item-1 active"><a>href="link4.html"fourth item</a></li>
     <li class="item-0"><a>href="link5.html"fifth item</a></li>
    </ul>
</div>
"""

html2 = """
<div class="wrap">
  <div id="container">
    <ul class="list">
     <li class="item-0">first item</li>
     <li class="item-1"><a href="link2.html"></a>second item</li>
     <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
     <li class="item-1 active"><a href="link4.html">fourth item</a></li>
     <li class="item-0"><a href="link5.html">fifth item</a></li>
    </ul>
  </div>
</div>
"""
doc = pq(html)
print(doc('li'))
print("--"*50)

doc2 = pq(url="http://baidu.com")
print(doc2('head'))
print("--"*50)

# 文件初始化
doc3 = pq(filename="demo.html")
print(doc3('li'))
print("--"*50)

# 基本CSS选择器
doc4 = pq(html)
print(doc4('#container .list li'))
print("--"*50)

# 查找元素
print("查找元素。。。")
doc5 = pq(html)
items = doc5('.list')
print(type(items))
print(items)
lis = items.find('li')
print(type(lis))
print(lis)

print("查找子元素。。。")
lis2 = items.children()
print(type(lis2))
print(lis2)
lis3 = items.children('.active')
print(type(lis3))
print(lis3)
print("--"*50)

print("查找父元素。。。")
doc6 = pq(html)
items6 = doc6('.list')
con6 = items6.parent()
print(type(con6))
print(con6)
print("--"*50)

print("查找全部父元素。。。")
doc7 = pq(html2)
items7 = doc7('.list')
con7 = items7.parents()
print(type(con7))
print(con7)
print("--"*50)
con8 = items7.parents('.wrap')
print(con8)
print("--"*50)

print("查找兄弟元素。。。")
lis3 = doc7('.list .item-0.active')
print(lis3)
print(lis3.siblings())
print(lis3.siblings('.active'))
print("--"*50)

print("获取属性。。。")
a = doc7('.item-0.active a')
print(a)
print(a.attr('href'))
print(a.attr.href)
print("--"*50)

print("获取文本。。。")
print(a.text())
print("--"*50)

print("获取HTML。。。")
a2 = doc7('.item-0.active')
print(a2)
print(a2.html())
