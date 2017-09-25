#!/user/bin/python3
# -*- coding:utf-8 -*-

"""
	通过某个字段将记录分组
	groupby()函数扫描整个序列并且超找连续相同值（或者根据指定key函数返回值相同）的元素序列、
	在每次迭代的时候，它会返回一个值和一个迭代器对象，这个迭代器对象可以生产元素值全部等于上面
	那个值得组中所有对象。
	一个非常重要的准备步骤就是要根据指定的字段将数据排序。因为groupby()仅仅检查连续的元素，如果
	事先并没有排序完成的话，分组函数将得不到想要的结果
"""
from operator import itemgetter
from itertools import groupby


rows = [
{'address': '5412 N CLARK', 'date': '07/01/2012'},
{'address': '5148 N CLARK', 'date': '07/04/2012'},
{'address': '5800 E 58TH', 'date': '07/02/2012'},
{'address': '2122 N CLARK', 'date': '07/03/2012'},
{'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
{'address': '1060 W ADDISON', 'date': '07/02/2012'},
{'address': '4801 N BROADWAY', 'date': '07/01/2012'},
{'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

rows.sort(key=itemgetter('date'))

for date, items in groupby(rows,key=itemgetter('date')):
	print(date)
	for i in items:
		print(' ',i)