#coding=utf-8
#/usr/bin/env python3

#装饰器
def w1(func):
    print("---func---1---")

    def inner(*args,**kwargs):
        print("---func_in---1---")
        func(*args,**kwargs)
        print("---func_in---2---")

    print("---func---2---")
    return inner



@w1
def f1(a,b,c,d):
    print("我是函数f1，我开始执行啦！！The result is : "+str(a+b+c+d))

f1(5,5,11,22)

