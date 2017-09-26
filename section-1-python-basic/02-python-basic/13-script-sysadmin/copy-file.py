#!/user/bin/python3
# -*- coding:utf-8 -*-

"""
    需求1：
        赋值或移动文件和目录，又不想调用shell命令
"""
import shutil
import os.path

filename = ''



"""
    需求2：
        创建或解压常见格式的归档文件（比如.tar,.tgz,.zip）
"""
shutil.unpack_archive('Python-3.3.0.tgz')
# make_archive()的第二个参数是期望的输出格式，可以使用get_archive_formats()获取所有支持的归档格式列表
shutil.make_archive('py33', 'zip', 'Python-3.3.0.tgz')

