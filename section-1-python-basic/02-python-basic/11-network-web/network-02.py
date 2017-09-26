#!/user/bin/python3
# -*- coding:utf-8 -*-
import ipaddress

"""
    需求1：
        将一个CIDR网络地址比如"123.45.67.89/27",转换成它所代表的所有IP
        可以使用ipaddress模块
"""
net = ipaddress.ip_network('123.45.67.64/27')
for ip_address in net:
    print(ip_address)
net2 = ipaddress.ip_network('192.168.15.0/24')
ip_list = []
for ip_address in net2:
    # print(ip_address)
    ip_list.append(ip_address)
print(ip_list)
