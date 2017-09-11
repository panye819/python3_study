#coding=utf-8
#/usr/bin/env python3

def createNum():
	print("---start---")
	a,b=0,1
	for i in range(5):
		print("---1---")
		yield b
		print("---2---")
		a,b=b,a+b
		print("---3---")
	print("---stop---")


a=createNum()

ret=a.__next__()
print(ret)


