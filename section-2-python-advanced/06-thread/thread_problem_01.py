#!/user/bin/python3
#!coding=utf-8

import time
from threading import Thread
#线程之间共享全局变量，如果全局变量没有控制好，容易产生问题
g_num=0

def work1():
	global g_num
	for i in range(1000000):
		g_num +=1
	# print("---in work1,g_num is %d---"%g_num)
	print("---test1--g_num=%d"%g_num)
def work2():
	global g_num
	for i in range(1000000):
		g_num +=1

	print("---test1--g_num=%d"%g_num)

print("---线程创建之前 g_num is %d---"%g_num)
t1=Thread(target=work1)
t1.start()

# time.sleep(3) 注销这行语句之后，结果与没有注释之前不一样

t2=Thread(target=work2)
t2.start()

