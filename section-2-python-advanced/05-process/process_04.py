#!/user/bin/python3
#!coding=utf-8
import os
import time


ret=os.fork()
num=100
if ret==0:
	print("----process-1---")
	num=num+100
	print("----process-1-num=%d---"%num)
else:
	print("----process-2---")
	
	print("----process-2-num=%d---"%num)

