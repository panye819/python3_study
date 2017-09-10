#coding=utf-8
#/usr/bin/env python3

#装饰器对带有返回值的函数进行装饰
def w1(func):
    print("---func---1---")

    def inner():
        print("---func_in---1---")
        #用一个变量接收f1的返回值

        x= func()
        print("---func_in---2---")
        return x
    print("---func---2---")
    return inner



@w1
def f1():
    print("我是函数f1，我开始执行啦！！")
    return "python3"


ret=f1()
print("test return value is %s" %ret)

