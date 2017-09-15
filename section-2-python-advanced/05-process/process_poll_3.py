#!/user/bin/python3
#!coding=utf-8

from multiprocessing import Pool
import time,os
import random

"""
进程池

"""

def worker(num):
    for i in range(5):
        print("===pid=%d==num=%d"%(os.getpid(),num))
        time.sleep(1)   #

po=Pool(3)

for i in range(10):
    print("---%d---"%i)
    #Pool.apply_async(要调用的目标,(传递给目标的参数元组))
    #每次循环都会用空闲出来的子进程去调用目标
    po.apply(worker,(i,))


#关闭进程池，关闭后po不再接受新的请求
po.close()
#等待po中所有子进程执行完毕，必须在close语句之后
po.join()


