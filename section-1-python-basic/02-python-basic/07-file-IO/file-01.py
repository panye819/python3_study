#!/user/bin/python3
# -*- coding:utf-8 -*-


"""
    需求1：
        将print()函数的输出，重定向到一个文件中去，可以在print()函数中指定file关键字参数
"""
with open('test.txt', 'wt') as f:
    print("Hello World!", file=f)
print("------------------我是分割线------------------")

"""
    需求2：
        想使用print()函数输出数据，但是想改变默认的分隔符或者行尾符，可以使用sep和end关键字参数
"""
print('ACME', 50, 91.5)
print('ACME', 50, 91.5, sep=',')
print('ACME', 50, 91.5, sep=',', end='!!\n')
# 使用end参数也可以在输出中禁止换行
for i in range(5):
    print(i)
    print(i, end=' ')
print("------------------我是分割线------------------")

"""
    需求3：
        想向一个文件中写入数据，但是前提是这个文件在文件系统中不存在，也就是不允许覆盖已存在的内容
"""
with open('test1.txt', 'xt') as f:
    f.write('Hello\n')
