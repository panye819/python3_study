#!/user/bin/python3
#!coding=utf-8

"""
	async

"""

from multiprocessing import Pool
import os,time

def test():
	print("---进程池中的进程---pid=%d,ppid=%d--" %(os.getpid(),os.getppid()))
	for i in range(3):
		print("----%d---"%i)
		time.sleep(1)
	return "haha"

def test2(args):
	print("---callback func--pid=%d"%os.getpid())
	print("---callback func--pid=%s"%args)


pool = Pool(3)

pool.apply_async(func=test,callback=test2)

while True:
	time.sleep(1)
	print("---主进程-pid=%d----"%os.getpid())
