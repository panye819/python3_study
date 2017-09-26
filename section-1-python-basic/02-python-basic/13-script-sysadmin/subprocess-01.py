#!/user/bin/python3
# -*- coding:utf-8 -*-

"""
    需求1：
        运行脚本时需要输入一个密码，此脚本时交互式的，不能讲密码再脚本中硬编码，而是需要弹出一个密码输入提示
        让用户自己输入
"""
import subprocess


out_bytes = subprocess.check_output(['ls', '-a'])
out_text = out_bytes.decode('utf-8')
print(out_text)
print("------------------我是分割线------------------")

"""
    需求2：
        获取当前终端的大小以便正确的格式化输出
"""

