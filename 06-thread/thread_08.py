#!/user/bin/python3
#!coding=utf-8

#非全局变量在不同线程中不会互相影响

from threading import Thread
import threading
import time

def work1():
	name = threading.current_thread().name
	print("----thread name is %s ----"%name)
	g_num = 100
	if name == "Thread-1":
		g_num += 1
	else:
		time.sleep(2)
	print("---thread is %s ----g_num=%d"%(name,g_num))

t1=Thread(target=work1)
t1.start()

t2=Thread(target=work1)
t2.start()
