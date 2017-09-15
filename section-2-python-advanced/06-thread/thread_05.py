#!/user/bin/python3
#!coding=utf-8

import time
from threading import Thread
#线程之间共享全局变量
g_num=0
g_flag=1

def work1():
	global g_num
	global g_flag
	if g_flag == 1: 
		for i in range(1000000):
			g_num +=1
		
		g_flag=0
	print("---work1--g_num=%d"%g_num)
def work2():
	global g_num
	# global g_flag
	while True:
		if g_flag != 1:
			for i in range(1000000):
				g_num +=1
			break

	print("---work2--g_num=%d"%g_num)

print("---线程创建之前 g_num is %d---"%g_num)

t1=Thread(target=work1)
t1.start()

# time.sleep(1)

t2=Thread(target=work2)
t2.start()

# print("---程序运行结束之后 g_num is %d---"%g_num)
