#!/user/bin/python3
# -*- coding:utf-8 -*-


class Cat:
    def __init__(self, new_name, new_age):
        self.name = new_name
        self.age = new_age

    def eat(self):
        print("Cat is eating...")

    def drink(self):
        print("Cat is drinking...")

    def introduce(self):
        print("%s的年龄是%s" % (self.name, self.age))


tom = Cat("汤姆", 40)
tom.eat()
tom.drink()
tom.introduce()

print("-" * 40)

lanmao = Cat("蓝猫", 10)
lanmao.introduce
