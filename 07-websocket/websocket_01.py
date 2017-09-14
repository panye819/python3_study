#!/user/bin/python3
#!coding=utf-8
"""
    socket:
           简称套接字， 是进程间通信的一种方式，它与其他进程间通信的一个主要不同是它能实现不同主机间的的进程间的通信。

"""
from socket import *

#创建套接字
udpsocket = socket(AF_INET,SOCK_DGRAM)

#准备接收方的地址
sendAddr = ('')

#从键盘获得数据
sendData = raw_input("请输入要发送的数据：")

#发送到接收方


