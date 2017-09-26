#!/user/bin/python3
# -*- coding:utf-8 -*-
from urllib import request, parse


"""
    需求1：
        需要使用HTTP协议以客户端的方式访问多种服务
"""
url = 'http://httpbin.org/get'
headers = {
    'User-agent': 'none/ofyourbusiness',
    'Spam': 'Eggs'
}
parms ={
    'name1': 'value1',
    'name2': 'value2'
}

querystring = parse.urlencode(parms)
u = request.urlopen(url+'?'+querystring)
resp = u.read()
print(resp)
