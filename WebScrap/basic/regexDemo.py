import re
str_1 = "a1B2cDef"
content = "Hello 123 4567 World_This is a Regex Demo"
content2 = "Hello 1234567 World_This is a Regex Demo"
content3 = """Hello 1234567 World_This is 
                a Regex Demo"""
content4 = "price is $5.00"
res = re.match('^Hello\s\d{3}\s\d{4}\s\w{10}.*Demo$', content)
print(res)
print(res.group())
print(res.span())
print("--"*50)
res2 = re.match('^Hello.*Demo$', content)

# 泛匹配

print(res2)
print(res2.group())
print(res2.span())
print("--"*50)

# 匹配目标

res3 = re.match('^Hello\s(\d+)\sWorld.*Demo$', content2)
print(res3)
print(res3.group(1))
print(res3.span())
print("--"*50)

# 贪婪模式
res4 = re.match('^Hello.*(\d+).*Demo$', content2)
print(res4)
print(res4.group(1))
print("--"*50)

# 非贪婪模式 ?指定为非贪婪模式
res5 = re.match('^Hello.*?(\d+).*Demo$', content2)
print(res5)
print(res5.group(1))
print("--"*50)

# 匹配模式
# 下面的语句无法匹配换行符
# res6 = re.match('^He.*?(\d+).*?Demo$', content3)
# 下面的语句可以匹配换行符
res6 = re.match('^He.*?(\d+).*?Demo$', content3, re.S)
print(res6)
print(res5.group(1))
print("--"*50)

res7 = re.match('price is \$5.00', content4)
print(res7)
print("--"*50)
