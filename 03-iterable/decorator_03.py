#coding=utf-8
#/usr/bin/env python3

#装饰器
def w1(func):
    print("开始装饰1......")
    def inner():
        print("开始验证权限1......")
        func()
    return inner
@w1
def f1():
    print("我是函数f1，我开始执行啦！！")

