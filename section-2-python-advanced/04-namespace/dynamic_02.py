#coding=utf-8
#/usr/bin/env python3

class Person(object):
    def __init__(self,newName,newAge):
        self.name=newName
        self.age=newAge
    def eat(self):
        print("---%s正在吃东西---"%self.name)

def run(self):
        print("---%s正在跑步---"%self.name)

p1=Person("p1",33)
p1.eat()

#p1.run=run

#虽然p1对象中的run熟悉已经指向了run函数，但是这句代码并不正确
#因为run属性指向的函数是后来添加的，建p1.run()的时候，并没有把
#p1当成第一个参数，导致后面函数调用的时候，出现缺少参数的问题。
import types

p1.run=types.MethodType(run,p1)
p1.run()


def sing(self):
    print("---%s正在唱歌---"%self.name)


p1.sing=types.MethodType(sing,p1)
p1.sing()
