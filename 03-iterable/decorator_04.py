#coding=utf-8
#/usr/bin/env python3

#装饰器
def w1(func):
    print("---func---1---")

    def inner():
        print("---func_in---1---")
        func()
        print("---func_in---2---")

    print("---func---2---")
    return inner
@w1
def f1():
    print("我是函数f1，我开始执行啦！！")

f1()

