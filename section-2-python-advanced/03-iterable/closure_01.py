#coding=utf-8
#/usr/bin/env python3
#定义一个函数
def test(number):
    #在函数内部再定义一个函数，并且这个函数内部用到了外面的变量，那么将
    #这个函数以及用到的一些变量称为闭包。
    def test_in(number_in):
        print("in test_in 函数，number_in is %d" %number_in)
        return number+number_in

   #其实这里返回的就是闭包的结果
   return test_in

#给test函数赋值，这个20就是给参数number赋值
ret=test(20)

#注意这里的100其实是给参数number_in赋值
print(ret(100))

#这里的200同样是给参数number_in赋值

print(ret(200))
