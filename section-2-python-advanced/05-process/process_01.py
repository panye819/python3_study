#!/user/bin/python3
#!coding=utf-8
import os
import time
"""
	fork的返回值非常特殊：
		父进程返回一个大于0的值，子进程返回的值等于0

"""

#下面的语句会创建一个新的进程
ret=os.fork()

if ret>0:
	i=1
	print("---父进程---%d"%os.getpid())
	print("1--Start...")
	while i<5:
		print("第 "+str(i)+" 次输出 Process-1")
		time.sleep(1)
		i+=1
	print("1--Stop...")
else:
	i=1
	print("---子进程---%d"%os.getppid())
	print("2--Start...")
	while i<5:
		print("第 "+str(i)+" 次输出 Process-2")
		time.sleep(1)
		i+=1
	print("2--Stop...")
