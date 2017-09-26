#!/user/bin/python3
# -*- coding:utf-8 -*-

"""
    需求1：
        需要一个设计到文件查找操作的脚本
"""
import os
import sys


def findfile(start, name):
    for relpath, dirs, files in os.walk(start):
        if name in files:
            full_path = os.path.join(start,relpath,name)
            print(os.path.normpath(os.path.abspath(full_path)))


if __name__ == '__main__':
    findfile(sys.argv[1], sys.argv[2])



