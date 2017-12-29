from pyquery import PyQuery as pq

html = """
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

# DOM操作

doc = pq(html)
li = doc('.item-0.active')
print(li)
print("--"*50)
li.remove_class('active')
print(li)
print("--"*50)
li.add_class('active')
print(li)
print("--"*50)

print("修改属性")
li.attr('name', 'link')
print(li)
print("--"*50)
li.css('font-size', '14px')
print(li)
print("--"*50)
