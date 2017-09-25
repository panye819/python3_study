#!/user/bin/python3
# -*- coding:utf-8 -*-
import re

line = 'asdf fjdk; afed, fjek,asdf, foo'

line_1 = re.split(r'[;,\s]\s*',line)
print(line_1)

"""
	检查字符串开头或者结尾的简单方法就是使用str.startwith()或者是str.endswith()方法
"""
filename = 'spam.txt'
url = 'http://www.python.org'
print(filename.endswith('.txt'))
print(filename.endswith('txt'))
print(filename.startswith('file:'))
print(url.startswith("http"))
print('*'*50)

text = 'yeah, but no, but yeah, but no, but yeah'

print(text.replace('yeah','yep'))

text2 = 'Today is 09/25/2017. PyCon starts 3/13/2013.'

print(re.sub(r'(\d+)/(\d+)/(\d+)',r'\3-\1-\2',text2))
print('*'*50)

#忽视大小写搜索

text3 = 'UPPER PYTHON, lower python, Mixed Python'
print(re.findall('python',text3,flags=re.IGNORECASE))
print(re.sub('python','snake',text3,flags=re.IGNORECASE))