#coding=utf-8
#/usr/bin/env python3

#LEGB规则：
#python使用LEGB的顺序来查找一个符号对应的对象
#locals-->enclosing function-->globals-->builtins
#locals:局部变量
#enclosing：外部嵌套函数的命名空间
#globals：全局变量
#builtins：内建

num=100
def test1():
    #num=200
    def test2():
     #   num=300
        print(num)
    return test2

ret=test1()
ret()
