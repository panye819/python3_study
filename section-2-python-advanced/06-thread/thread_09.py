#!/user/bin/python3
#!coding=utf-8

"""死锁问题:
	解决办法：
		1、银行家算法
		2、增加超时时间，acquire(True,2)
"""
import threading
import time

class MyThead1(threading.Thread):
	def run(self):
		if mutexA.acquire():
			print(self.name+'----do1---up---')
			time.sleep(1)

			if mutexB.acquire(True,2):
				print(self.name+'----do1---down---')
				mutexB.release()
			mutexA.release()

class MyThead2(threading.Thread):
	def run(self):
		if mutexB.acquire():
			print(self.name+'----do2---up---')
			time.sleep(1)

			if mutexA.acquire(True,2):
				print(self.name+'----do2---down---')
				mutexA.release()
			mutexB.release()

if __name__ == '__main__':
	mutexA = threading.Lock()
	mutexB = threading.Lock()

	t1=MyThead1()
	t2=MyThead2()

	t1.start()
	t2.start()