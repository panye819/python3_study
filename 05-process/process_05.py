#!/user/bin/python3
#!coding=utf-8
import os
import time


ret=os.fork()

if ret==0:
	print("----process-1---")
else:
	print("----process-2---")
	ret=os.fork()
	if ret==0:
		print("----process-11---")
	else:
		print("----process-22---")
# ret=os.fork()
# if ret==0:
# 	print("----process-11---")
# else:
# 	print("----process-22---")


