#!/user/bin/python3
#!coding=utf-8

import time
from threading import Thread
#线程之间共享全局变量
# g_num=100

def work1(nums):
	nums.append(44)
	print("---in work1---",nums)

def work2(nums):
	time.sleep(1)
	print("---in work2---",nums)

g_nums=[11,22,33]

t1=Thread(target=work1,args=(g_nums,))
t1.start()



t2=Thread(target=work2,args=(g_nums,))
t2.start()

