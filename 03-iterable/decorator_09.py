#coding=utf-8
#/usr/bin/env python3

#带参数的装饰器
def func_arg(arg=100):
    def func(functionName):

        def func_in():
            print("----记录日志----arg=%s"%arg)
            functionName()
        return func_in
    return func

#装饰器带参数，在原有装饰器的基础上，设置外部变量

#1、先执行func_arg("heihei")函数，这个函数return的结果是func这个函数的引用
#2、@func
#3、使用@func对test进行装饰


#@func_arg("heihei")
@func_arg()
def test():
    print("---test---")


test()
