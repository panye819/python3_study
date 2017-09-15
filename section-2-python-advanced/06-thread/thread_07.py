#!/user/bin/python3
#!coding=utf-8

from threading import Thread,Lock
import time

"""
互斥锁:
	创建锁：
		mutex=Lock()
	锁定：
		mutex.acquire([blocking])
		blocking的值为True，则当前线程会阻塞，直到获取到这个锁为止（默认为True）
		blocking的值为False，则当前线程不会阻塞
	释放：
		mutex.release()
"""

g_num=0


def work1():
	global g_num
	global g_flag
	mutex.acquire() 
	for i in range(1000000):
		g_num +=1
	mutex.release()
	
	print("---work1--g_num=%d"%g_num)

def work2():
	global g_num
	# global g_flag
	mutex.acquire()
	for i in range(1000000):
		g_num +=1
	mutex.release()
	print("---work2--g_num=%d"%g_num)

print("---线程创建之前 g_num is %d---"%g_num)

#创建锁，默认是没有上锁的
mutex=Lock()

t1=Thread(target=work1)

t1.start()

# time.sleep(1)

t2=Thread(target=work2)

t2.start()


# 
# print("---程序运行结束之后 g_num is %d---"%g_num)
