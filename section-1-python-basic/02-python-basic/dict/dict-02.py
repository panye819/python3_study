#!/user/bin/python3
# -*- coding:utf-8 -*-

"""
	构造一个字典，它是另外一个字典的子集
"""

#最简单的方法就是字典推导

prices = {
'ACME': 45.23,
'AAPL': 612.78,
'IBM': 205.55,
'HPQ': 37.20,
'FB': 10.75
}

p1 = {key:value for key ,value in prices.items() if value >200}

tech_name = {'AAPL','IBM','HPQ','MSFT'}

p2 = {key:value for key,value in prices.items() if key in tech_name}

print(p1)
print(p2)