from pyquery import PyQuery as pq

html = """
<div class="wrap">
  Hello, World
  <p>This is a parahraph.</P>
</div>
"""

# DOM操作

doc = pq(html)
li = doc('.wrap')
print(li.text())
li.find('p').remove()
print(li.text())
print("--"*50)
