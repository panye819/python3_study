#!/user/bin/python3
# -*- coding:utf-8 -*-

"""
	利用规则从一个数据序列中提取出需要的值或者是缩短序列
	itertools.compress() ，它以一个iterable对象和一个相对应的Boolean选择器序列作为输入参数。
	然后输出iterable 对象中对应选择器为True 的元素。
	当你需要用另外一个相关联的序列来过滤某个序列的时候，这个函数是非常有用的。
"""
values = ['1', '2', '-3', '-', '4', 'N/A', '5']

def is_int(val):
	try:
		x = int(val)
		return True
	except ValueError:
		return False

ivals = list(filter(is_int,values))

print(ivals)

addresses = [
'5412 N CLARK',
'5148 N CLARK',
'5800 E 58TH',
'2122 N CLARK',
'5645 N RAVENSWOOD',
'1060 W ADDISON',
'4801 N BROADWAY',
'1039 W GRANVILLE',
]
print(addresses)
counts = [ 0, 3, 10, 4, 1, 7, 6, 1]

from itertools import compress
more5 = [n >5 for n in counts]

print(more5)

print(list(compress(addresses,more5)))