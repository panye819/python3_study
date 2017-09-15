#!/user/bin/python3
#!coding=utf-8
import os
import time

#下面的语句会创建一个新的进程
ret=os.fork()

if ret==0:
	print("process--1--01---")
	time.sleep(1)
	print("process--1--02---")
	time.sleep(1)
	print("process--1--03---")
	time.sleep(1)
	print("process--1-Over....")
else:
	print("process--2--01---")
	time.sleep(1)
	print("process--2--02---")
	time.sleep(1)
	print("process--2--03---")
	time.sleep(1)
	print("process--2-Over....")

