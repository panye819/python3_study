#coding=utf-8
#/usr/bin/env python3

def line_conf(a,b):
    def line(x):
        return a*x+b
    return line
line1=line_conf(1,1)
line2=line_conf(4,5)

print(line1(5))
print('-'*30)
print(line2(5))
