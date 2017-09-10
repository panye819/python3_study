#coding=utf-8
#/usr/bin/env python3

class Person(object):
    def __init__(self,newName,newAge):
        self.name=newName
        self.age=newAge


laowang=Person("老王",30)
print(laowang.name)
print(laowang.age)


laowang.addr="Beijing"

print(laowang.addr)


laozhao=Person("老赵",33)
laozhao.addr="Hangzhou"
print(laozhao.addr)


Person.school="NJUT"

laowu=Person("老吴",44)
print(laowu.school)
