#!/user/bin/python3
# -*- coding:utf-8 -*-
"""
	现在有多个字典或者映射，如果需要将他们从逻辑上合并为一个单一的映射后执行某些操作，比如查找值或者
		检查某些值是否存在。
"""
a = {'x':1,'z':3}
b = {'y':2,'z':4}

from collections import ChainMap

c = ChainMap(a,b)

print(c['x'])
print(c['y'])
print(c['z'])
print(len(c))
print(list(c.keys()))
print(list(c.values()))