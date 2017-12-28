import re

content = """Hello 1234567 World_This is 
                a Regex Demo"""

# re.compile 将正则字符串编译成正则表达式对象，以便于复用该匹配模式

pattern = re.compile('Hello.*Demo', re.S)
res2 = re.match(pattern, content)
print(res2)
print("--"*50)


#

