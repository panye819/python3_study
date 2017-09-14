#!/user/bin/python3
#!coding=utf-8

"""
	GIL(Global Interpreter Lock)
		全局解释器锁，同一时刻，只有一个线程被调用
		如果想充分利用多核CPU，可以使用多进程

		使用C语言来解决GIL问题

"""

from ctypes import *
from threading import Thread

#加载动态库
lib = cdll.LoadLibrary("./libdeadLoop.so")

#创建一个子线程，让其执行c语言编写的函数，这个函数是一个死循环
t=Thread(target=lib.Deadloop)
t.start()
#主线程，也调用C语言编写的那个死循环函数
lib.DeadLoop()

while True:
	pass

