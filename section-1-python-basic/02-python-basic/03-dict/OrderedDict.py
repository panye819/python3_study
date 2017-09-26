#!/user/bin/python3
# -*- coding:utf-8 -*-

"""
	为了能控制字典中元素的顺序，可以使用collections模块中的OrderedDict类，在迭代操作时
	它会保持元素被插入的顺序
"""
from collections import OrderedDict
import json


def ordered_dict():
	d = OrderedDict()
	d['foo'] = 1
	d['bar'] = 2
	d['spam'] = 3
	d['grok'] = 4
	for key in d:
		print(key, d[key])

ordered_dict()
json.dumps(ordered_dict())
