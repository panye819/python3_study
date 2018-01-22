# coding=utf-8


"""

    如果a+b+c=1000,且a^2+b^2=c^2(a,b,c为自然数)，如何求出所有a,b,c可能的组合？

"""

import time
# 第一版，a,b,c逐位试探，最后的到结果，一共运行了163秒。
"""start_time = time.time()
for a in range(0, 1001):
    for b in range(0, 1001):
        for c in range(0,1001):
            if a+b+c == 1000 and a**2+b**2 == c**2:
                print("a, b, c:%d, %d, %d " % (a, b, c))

end_time = time.time()

print("times:%d" % (end_time-start_time))
print("Finished!")
"""
# 第二版，a,b确定之后，c就是1000-a-b,修改上面的代码如下：
# 整个执行过程只有1秒钟，执行效率比第一版代码大幅提高
start_time = time.time()
for a in range(0, 1001):
    for b in range(0, 1001):
        c = 1000-a-b
        if a**2+b**2 == c**2:
            print("a, b, c:%d, %d, %d " % (a, b, c))

end_time = time.time()

print("times:%d" % (end_time - start_time))
print("Finished!")

"""
    算法效率的衡量：
        时间复杂度与"大O记法"
        
"""