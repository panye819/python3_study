#!coding=utf-8
from multiprocessing import Manager, Pool
import os, time, random

# 写数据进程执行的代码:
def writer(q):
    print("writer启动(%s),父进程为(%s)"%(os.getpid(),os.getppid()))
    for value in "dongGe":
        print 'Put %s to queue...' % value
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:
def reader(q):
    print("reader启动(%s),父进程为(%s)"%(os.getpid(),os.getppid()))
    for i in range(q.qsize()):
        print("reader从Queue获取到消息：%s"%q.get(True))

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    print("(%s) Start..."%os.getpid())
    q = Manager().Queue()
    po=Pool()
    po.apply(writer,(q,))
    po.apply(reader,(q,))
    po.close()
    po.join()
    print("(%s) End"%os.getpid())