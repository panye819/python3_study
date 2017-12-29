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
li = doc('li:first-child')
print(li)
print("--"*50)
li = doc('li:last-child')
print(li)
print("--"*50)
li = doc('li:nth-child(2)')
print(li)
print("--"*50)
li = doc('li:gt(2)')
print(li)
print("--"*50)
li = doc('li:nth-child(2n)')
print(li)
print("--"*50)
li = doc('li:contains(second)')
print(li)
print("--"*50)
