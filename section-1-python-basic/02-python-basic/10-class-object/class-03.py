#!/user/bin/python3
# -*- coding:utf-8 -*-


"""
    需求1：
        想改变对象实例的打印或显示输出，让它们更具可读性
"""


class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)

    def __str__(self):
        return '({0.x!r}, {0.y!r})'.format(self)
p = Pair(3, 4)
print(p)

print("------------------我是分割线------------------")

"""
    需求2：
        测试一个文件是否存在
"""

print('*'*50)
# 还能进一步获得元数据：比如文件大小或者修改日期。

print("------------------我是分割线------------------")

"""
    需求3：
        获取文件夹中的所有文件列表
"""
