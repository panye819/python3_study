#coding=utf-8
#/usr/bin/env python3

#装饰器
def w1(func):
    def inner():
        print("----1-----")
        return "<b>"+func()+"</b>"
    return inner
def w2(func):
    def test2():
        print("----2----")
        return "<i>"+func()+"</i>"
    return test2
@w1
@w2
def f1():
    print("----3----")
    return "hello world-3"

ret=f1()
print(ret)
