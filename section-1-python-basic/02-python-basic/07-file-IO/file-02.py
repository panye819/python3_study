#!/user/bin/python3
# -*- coding:utf-8 -*-

import os
import time
"""
    需求1：
        需要使用路径名来获取文件名，目录名，绝对路径等
"""
path = '/Users/beazley/Data/data.csv'
print(os.path.basename(path))
print(os.path.dirname(path))
print(os.path.join('tmp', 'data', os.path.basename(path)))
print('*'*50)
path_1 = '~/Data/data.csv'
print(os.path.expanduser(path_1))
print(os.path.splitext(path_1))
print("------------------我是分割线------------------")

"""
    需求2：
        测试一个文件是否存在
"""
print(os.path.exists('test.txt'))
print(os.path.exists('test1.txt'))
print(os.path.exists('test2.txt'))
print('*'*50)
# 还能进一步测试这个文件是什么类型的。
print(os.path.isfile('/etc/passwd'))
print(os.path.isdir('/etc/passwd'))
print(os.path.islink('/etc/passwd'))
print(os.path.realpath('/usr/local/bin/python3'))
print('*'*50)
# 还能进一步获得元数据：比如文件大小或者修改日期。
print(os.path.getsize('/etc/passwd'))
print(os.path.getatime('/etc/passwd'))
print(time.ctime(os.path.getatime('/etc/passwd')))
print(os.path.getctime('/etc/passwd'))
print(time.ctime(os.path.getctime('/etc/passwd')))
print(os.path.getmtime('/etc/passwd'))
print(time.ctime(os.path.getmtime('/etc/passwd')))
print("------------------我是分割线------------------")

"""
    需求3：
        获取文件夹中的所有文件列表
"""
somedir = '/Users/castlepan/Study-Code/python3_study/section-1-python-basic'
names = [name for name in os.listdir(somedir)
         if os.path.isfile(os.path.join(somedir, name))]
dirnames = [name for name in os.listdir(somedir)
         if os.path.isdir(os.path.join(somedir, name))]
print(names)
print(dirnames)
print(os.listdir(somedir))
