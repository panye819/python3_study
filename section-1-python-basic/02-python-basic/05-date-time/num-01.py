#!/user/bin/python3
# -*- coding:utf-8 -*-
from decimal import Decimal, localcontext
"""
    需求1：
        对于浮点数执行指定精度的舍入运算
"""
num = 1.23456
print(round(num, 1))
print(round(num, 2))
print(round(num, 3))
print('-'*50)

# 当一个值刚好在两个边界的中间的时候，round函数返回离它最近的偶数，也就是说，对1.5或者2.5
# 的舍入运算都会得到2
print(round(1.5))
print(round(2.5))
print('-'*50)

# 传给round()函数的ndigits参数可以是负数，这种情况下，舍入运算会作用在十位、百位、千位等上面。
num1 = 1627731
print(round(num1, -1))
print(round(num1, -2))
print(round(num1, -3))
print(round(num1, -4))
print("------------------我是分割线------------------")

"""
    需求2：
        对于浮点数执行精确的计算操作，并且不希望有任何小误差的出现
"""
a = 4.2
b = 2.1
print(a+b)  # 结果为6.300000000000001
print((a+b) == 6.3)  # 输出结果为False
# 出现这种现象的原因是由底层CPU和IEEE 754标准通过自己的浮点单位去执行算数时的特征。
# 由于Python的浮点数据类型使用底层表示存储数据，因此这种误差是无法避免的
# 如果你想更精确，可以使用decimal模块

a1 = Decimal('4.2')
b1 = Decimal('2.1')
print(a1+b1)
print("a1+b1 equals : "+str(a1+b1))

# decimal模块的一个主要特征是允许你控制计算的每一个方面，包括数字位数和四舍五入运算
# 为了这样做，你先要创建一个本地上下文并更改它的设置

a2 = Decimal('1.3')
b2 = Decimal('1.7')

print(a2/b2)
with localcontext() as ctx:
    ctx.prec = 3
    print(a2/b2)
with localcontext() as ctx:
    ctx.prec = 50
    print(a2/b2)
