#!/user/bin/python3
# -*- coding:utf-8 -*-

#如果你想要合并的字符串是在一个序列或者iterable中，那么最快的方式可就是使用join()方法

parts = ['Is', 'Chicago', 'Not', 'Chicago?']

print(' '.join(parts))
print('-'.join(parts))
print(','.join(parts))
print('*'*50)
#如果仅仅只是合并少数几个字符串，使用加号“+”通常已经足够了
a = 'Is Chicago'
b = 'Not Chicago?'
print(a+' '+b)

#如果你想在源码中将两个字面字符串合并起来，你只要简单的将他们放在一起
print('*'*50)
str1 = 'Hello' ' World'
print(str1)

#创建一个内嵌变量的字符串，变量被它的值所表示的字符串替换掉
print('*'*50)
str2 = '{name} has {n} messages...'
print(str2.format(name='Guido',n=37))
print('*'*50)
name = 'Guido'
n = 37
print(str2.format_map(vars()))