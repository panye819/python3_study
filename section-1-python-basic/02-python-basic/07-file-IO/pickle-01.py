#!/user/bin/python3
# -*- coding:utf-8 -*-
import pickle

"""
    需求1：
        需要将一个Python对象序列化为一个字节流，以便将它保存到一个文件、存储到数据库或者通过网络传输
        对于序列化最简单的做法就是使用pickle模块
"""
shoplistfile = 'shoplist.data'

shoplist = ['apple', 'mango', 'carrot']

f = open(shoplistfile, 'wb')
pickle.dump(shoplist, f)
f.close()
del shoplist

f = open(shoplistfile,'rb')
storedlist = pickle.load(f)
print(storedlist)
# 千万不要对不信任的数据使用pickle.load，因为pickle在加载时有一个副作用就是它会自动加载相应模块并构造实例对象
# 如果关键字知道pickle的工作原理，就可以构造出一个恶意的数据导致Python执行随意指定的系统目录
# 因此，一定要保证pickle只在相互之间可以认证对方的解析器的内部使用
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
