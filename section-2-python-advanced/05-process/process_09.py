#!/user/bin/python3
#!coding=utf-8
from multiprocessing import Process
import time
import random

def test():
	for i in range(random.randint(1,5)):
		print("---%d---"%i)
		time.sleep(1)

p = Process(target=test)

p.start()

#当前主进程会等待子进程执行完毕之后才会结束，阻塞，如果join里面有数字参数，则在此时间后
#无论子进程是否结束，主进程直接退出
p.join(2)
#terminal()方法，直接结束进程

time.sleep(2)
print("----main----")