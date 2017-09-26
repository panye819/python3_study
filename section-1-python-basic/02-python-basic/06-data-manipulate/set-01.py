#!/user/bin/python3
# -*- coding:utf-8 -*-

from collections import Counter
"""
	如果仅仅是想消除重复元素，通常可以简单的构造一个集合

"""
a = [1,5,2,1,9,1,5,10]

print(set(a))

print('-'*40)

"""
	查找序列中出现次数最多的元素
"""
words = [
'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
'my', 'eyes', "you're", 'under'
]

word_counts = Counter(words)

# top_three = word_counts.most_common(3)
top_three = word_counts.most_common()

print(top_three)
print('-'*40)
"""
	依据某个或几个字典字段来排序一个字典列表
"""
from operator import itemgetter
rows = [
{'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
{'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
{'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
{'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

rows_by_fname = sorted(rows,key=itemgetter('fname'))
rows_by_uid = sorted(rows,key=itemgetter('uid'))
rows_by_lfname = sorted(rows,key=itemgetter('lname','fname'))

print(rows_by_fname)
print('*'*40)
print(rows_by_uid)
print('*'*40)
print(rows_by_lfname)
print('-'*40)