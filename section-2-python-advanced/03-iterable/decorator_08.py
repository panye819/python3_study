#coding=utf-8
#/usr/bin/env python3

#通用装饰器
def w1(func):
    print("---func---1---")

    def func_in(*args,**kwargs):
        ret = func(*args,**kwargs)
        return ret
    return func_in

@w1
def f1():
    print("我是函数f1，我开始执行啦！！")
    return "common_return"
@w1
def test2():
    print("----test2----")
@w1
def test3(a):
    print("----test3----a=%d"%a)

ret=f1()
print("test return value is %s" %ret)
print("-"*30)


test3(11)
