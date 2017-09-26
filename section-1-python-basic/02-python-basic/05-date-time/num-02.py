#!/user/bin/python3
# -*- coding:utf-8 -*-

"""
    需求1：
        为了将整数转换为二进制、八进制或者十六进制的文本串，可以分别使用bin(),oct()或hex()函数
"""
num = 1234
print(bin(num))
print(oct(num))
print(hex(num))
# 如果不想输出0b,0o或者0x前缀的话，可以使用format()函数
print(format(num, 'b'))
print(format(num, 'o'))
print(format(num, 'x'))
print("------------------我是分割线------------------")

"""
    需求2：
        假如你的程序需要处理一个拥有128位长的16个元素的字节字符串，为了将bytes解析为整数
        使用int.form_bytes()方法，并指定字节顺序
"""
data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
print(len(data))
print(int.from_bytes(data, 'little'))
print(int.from_bytes(data, 'big'))

# 为了将一个大整数转换为一个字节字符串，使用int.to_bytes()方法，并指定字节数和字节顺序
num2 = 94522842520747284487117727783387188
print(num2.to_bytes(16,'big'))
print(num2.to_bytes(16, 'little'))
