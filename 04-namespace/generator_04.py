#coding=utf-8
#/usr/bin/env python3


class Person(object):
    __slots__=("name","age","addr")



P=Person()

P.name="laowang"
P.age=33
P.addr="Nanjing"


print(P.name+" "+str(P.age)+" "+P.addr)

P.tel="123456"
print(P.tel)
