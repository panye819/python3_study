#coding=utf-8
#/usr/bin/env python3

#生成器：
#   在python中，这种一边循环一边计算的机制，称为生成器 generator


#a = [ x*2 for x in range(5)]

g=(x*2 for x in range(1000))

print("g is ",g)

print("-"*30)
#当一个函数中出现yield关键字的时候，这个函数就不再是普通的函数，而是生成器

def createNum():
    print("---start---")
    a,b=0,1
    for i in range(5):
        #程序执行到这里的时候，会暂停，然后返回yield后面的值
        yield b
        a,b=b,a+b
    print("---stop---")

a=createNum()
next(a)
