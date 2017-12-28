import re

# re.sub 替换字符串中每一个匹配的子串后，返回替换后的字符串

content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
res = re.sub('\d+', '', content)
print(res)
print("--"*40)

res2 = re.sub('(\d+)', r'\1 8910', content)
print(res2)
print("--"*40)

