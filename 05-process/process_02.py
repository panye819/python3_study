#!/user/bin/python3
#!coding=utf-8
import os
import time

#下面的语句会创建一个新的进程
ret=os.fork()
print(ret)
if ret>0:
	print("---父进程---%d"%os.getpid())
else:
	print("---子进程---%d--%d"%(os.getpid(),os.getppid()))

print("Over....")