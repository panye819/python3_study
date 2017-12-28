import requests
# from requests.auth import HTTPBasicAuth

# response = requests.get("https://github.com/favicon.ico")
# with open("/Users/castlepan/Downloads/demofile/favicon.ico", 'wb') as f:
#     f.write(response.content)
#     f.close()

print("--"*40)

res1 = requests.get("http://www.jianshu.com")

print(type(res1.status_code), res1.status_code)
print(type(res1.headers), res1.headers)
print(type(res1.cookies), res1.cookies)
print(type(res1.url), res1.url)
print(type(res1.history), res1.history)

print("--"*40)

res2 = requests.get("http://www.jianshu.com")
print("The return code is not 200") if not res2.status_code == 200 else print("Request Successfully")
print("--"*40)
res3 = requests.get("http://www.jianshu.com/hello.html")
exit() if not res3.status_code == requests.codes.not_found else print("404 Not Found")
print("--"*40)

s = requests.session()
s.get("http://httpbin.org/cookies/set/number/123456789")
res4 = s.get("http://httpbin.org/cookies")
print(res4.text)
print("--"*40)

res5 = requests.get("https://www.12306.cn")
print(res5.status_code)

# urllib3.disable_warnings()
res6 = requests.get("https://www.12306.cn", verify=False)
print(res6.status_code)

