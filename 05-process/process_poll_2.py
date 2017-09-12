#!/user/bin/python3
#!coding=utf-8

from multiprocessing import Pool
import time,os
import random

def worker(num):
    for i in range(5):
        print("===pid=%d==num=%d"%(os.getpid(),num))
        time.sleep(1)

po=Pool(3)

for i in range(5):
    print("---%d---"%i)
    po.apply_async(worker(i,))


#关闭进程池，关闭后po不再接受新的请求
po.close()
#等待po中所有子进程执行完毕，必须在close语句之后
po.join()


