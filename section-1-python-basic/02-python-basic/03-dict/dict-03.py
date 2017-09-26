#!/user/bin/python3
# -*- coding:utf-8 -*-

"""
   可以通过下标访问列表或者元组中的元素，但这样有时候会让你的代码难以阅读，于是可以通过名称来访问元素
   collection.nametuple()函数通过使用一个普通的元组对象来帮你解决这个问题
   		这个函数实际上是一个返回Python中标准元组类型子类的一个工厂方法。
   		你需要传递一个类型名和你需要的字段给它，然后它会返回一个类，你可以初始化这个类，为你定义的
   		字段传递值等。

"""
from collections import namedtuple

Subscriber = namedtuple('Subscriber',['addr','joined'])

sub = Subscriber('test@demo.com','2012-10-19')
print(sub)
print(sub.addr)
print(sub.joined)

print('*'*50)

print(len(sub))
addr,joined = sub
print(addr)
print(joined)

#一个命名元组是不可更改的，所以下面的命令执行会报错
# AttributeError: can't set attribute

# sub.addr = "test1@demo.com"
"""
	如果确实需要改变属性，那么可以使用命名元组实例的_replace()方法,
"""
sub = sub._replace(addr='test1@demo.com')
print(sub.addr)
print('*'*50)
"""
	replace() 方法还有一个很有用的特性就是当你的命名元组拥有可选或者缺失字段时候，
		它是一个非常方便的填充数据的方法。你可以先创建一个包含缺省值的原型元组，
		然后使用replace() 方法创建新的值被更新过的实例。
"""
Stock = namedtuple('Stock',['name','shares','price','date','time'])
stock_prototype = Stock('',0,0.0,None,None)

def dict_to_stock(s):
	return stock_prototype._replace(**s)
a = {'name':'ACME','shares':100,'price':123.45}
print(dict_to_stock(a))
b = {'name':'ACME','shares':100,'price':123.45,'date':'12/17/2012'}
print(dict_to_stock(b))