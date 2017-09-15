#coding=utf-8
#/usr/bin/env python3

#装饰器
def w1(func):
    def inner():
        print("-----正在验证权限")
        print("-"*30)
        print("验证成功，程序继续运行。。。")
        func()
    return inner
def w2(func):
    def test2():
        print("第二个验证程序")
        func()
    return test2
@w1
@w2
def f1():
    print("This is f1")
@w1
@w2
def f2():
    print("This is f2")
@w1
def f3():
    print("This is f3")

@w1
def f4():
    print("This is f4")

f1()
f2()
f3()
f4()
