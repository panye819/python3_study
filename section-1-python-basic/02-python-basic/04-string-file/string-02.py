#!/user/bin/python3
# -*- coding:utf-8 -*-
"""
    需求1：
        想去掉文本字符串开头，结尾或者中间不想要的字符，比如空白
"""

s = ' hello world \n'

print(s)
print(s.strip())
print(s.lstrip())
print(s.rstrip())


t = '----hello===='

print(t)
print(t.strip())
print(t.lstrip('-'))
print(t.rstrip('='))

# 以上操作不会对字符串产生影响，下面的语句依然会打印除原始字符串

print(s)
print(t)
print("------------------我是分割线------------------")
"""
    需求2：
        通过某种对齐方式来格式化字符串
"""
text = 'Hello world!'

print("'"+text.ljust(20)+"'")
print("'"+text.rjust(20)+"'")
print("'"+text.center(20)+"'")
print("*"*50)
# 所有这些方法还可以接受一个可选的填充字符
print("'"+text.rjust(20, '=')+"'")
print("'"+text.center(20, '*')+"'")
print("*"*50)
# 函数format()同样可以用来很容易的对齐字符串。你要做的就是使用<,>或者^字符后面紧跟一个指定的宽度。
print("'"+format(text, '>20')+"'")
print("'"+format(text, '<20')+"'")
print("'"+format(text, '^20')+"'")
# 当格式化多个值时，这些格式化代码也可以被用于format()方法中
print("'"+'{:>10s} {:>10s}'.format('Hello', 'World')+"'")
# format()函数的一个好处是它不仅适用于字符串，它还可以用来格式化任何值，使它变得非常通用
num = 1.2345
print(format(num, '>10'))
print(format(num, '^10.2f'))
print("------------------我是分割线------------------")
"""
    需求3：
        将几个小的字符串合并为一个大的字符串
"""
parts = ['Is', 'Chicago', 'Not', 'Chicago?']
print(' '.join(parts))
print(''.join(parts))
print(','.join(parts))
print("------------------我是分割线------------------")
"""
    需求4：
        将一些长字符串，以指定的列宽将他们重新格式化
"""
s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."

import textwrap
print(textwrap.fill(s, 70))
print(textwrap.fill(s, 40))
print(textwrap.fill(s, 40, initial_indent='**'))
print(textwrap.fill(s, 40, subsequent_indent='---'))




