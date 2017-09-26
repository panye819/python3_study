#!/user/bin/python3
# -*- coding:utf-8 -*-

"""
    需求1：
        希望你的脚本可以接受任何用户认为最简单的输入方式，包括将命令行的输出通过管道传递给该脚本
        重定向文件到该脚本，或者在命令行中传递一个文件名或者文件名列表给该脚本
        可以使用Python内置的fileinput模块
"""
import fileinput
import sys

with fileinput.input('/etc/passwd') as f:
    for line in f:
        print(f.filename(), f.lineno(), line, end='')
print("------------------我是分割线------------------")

"""
    需求2：
        想向标准错误打印一条消息并返回某个非零值来终止程序运行
"""
sys.stderr.write('It failed!\n')
raise SystemExit(111)
