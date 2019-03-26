# from urllib import request, parse

# url = 'http://httpbin.org/post'
#
# hearders={
#     'User-Agent': '',
#     'Host':'httpbin.org'
# }
#
# mdict = {
#     'name': 'Germey'
# }
#
# data = bytes(parse.urlencode(mdict), encoding='utf-8')
# req = request.Request(url=url, data=data, headers=hearders, method='POST')
# response = request.urlopen(req)
# print(response.read().decode('utf-8'))

# import urllib.request
# response = urllib.request.urlopen('http://www.baidu.com')
# # print(response.read().decode('utf-8'))
# print('#######')
# # print(response.read())
# print('######')
# print(response.read().decode('utf-8'))

# import urllib.parse
# import urllib.request
# data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
# r = urllib.request.urlopen('http://httpbin.org/post', data=data)
# print(r.read())

# import socket
# import urllib.request
# import urllib.error
#
# try:
#     response = urllib.request.urlopen('http://httpbin.org/get', timeout=3)
# except urllib.error.URLError as e:
#     if isinstance(e.reason, socket.timeout):
#         print('time out')


# import urllib.request
#
# response = urllib.request.urlopen('http://www.python.org', timeout=5)  # type: urllib.request
#
# print(response.status)
# print(response.getheaders())
# print(response.getheader('server'))


# import urllib.request
#
# request = urllib.request.Request('https://python.org')
# response = urllib.request.urlopen(request)
# print(response.read().decode('utf-8'))

# import urllib.request
# import urllib.parse
#
# url = 'http://httpbin.org/post'
# headers = {
#     'user-agent': '',
#     'host': 'httpbin.org'
# }
#
# dict = {
#     'name': 'WangPengchao'
# }
#
# data = bytes(urllib.parse.urlencode(dict), encoding='utf8')
# req = urllib.request.Request(url=url, data=data, method='POST')
# req.add_header('user-agent', '')
# req.add_header('host', 'httpbin.org')
# response = urllib.request.urlopen(req)
# print(response.read().decode('utf-8'))

# import urllib.parse
#
# values={}
# values['usename'] = 'wpc'
# values['password'] = '123456'
#
# # usename=wpc&password=123456
# values2 = {'usename': 'wpc', 'password': '123456'}
# url = 'http://www.baidu.com'
#
# data = urllib.parse.urlencode(values2)
# print(data)
#
# print(values)

# import urllib.request
#
# response = urllib.request.urlopen('http://www.python.org')
# print(response.getheaders())


# import urllib.request
#
# proxy_handler = urllib.request.ProxyHandler(
#     {'http': 'http://127.0.0.1:9743',
#      'https': 'https://127.0.0.1:9743'}
# )
# opener = urllib.request.build_opener(proxy_handler)
# response = opener.open('http://www.baidu.com')
# # print(response.read())


# import http.cookiejar
# import urllib.request
#
# cookie = http.cookiejar.CookieJar()
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
#
# for item in cookie:
#     print(item.name+'='+item.value)



# import urllib.request
# import urllib.parse
# import http.client
# response = urllib.request.urlopen('http://www.baidu.com')
# print(type(response))
# print(response.closed)
#
# print(dir(urllib.parse))


# import urllib.request
#
# request = urllib.request.Request(url='https://httpbin.org/get')
# print(type(request))
#
# response = urllib.request.urlopen(url=request)
# print(response.read().decode('utf-8'))


# from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
# from urllib.error import URLError
#
# username = 'username'
# password = 'password'
# url = 'http://www.baidu.com'
#
# p = HTTPPasswordMgrWithDefaultRealm()
# p.add_password(None, url, username, password)
#
# auth_handler = HTTPBasicAuthHandler(p)
#
# opener = build_opener(auth_handler)
#
# try:
#     result = opener.open(url)
#     html = result.read().decode('utf-8')
#     print(html)
# except URLError as e:
#     print(e.reason)



# import urllib.request
# import http.cookiejar
#
# cookie = http.cookiejar.CookieJar()
# cookirHandler = urllib.request.HTTPCookieProcessor(cookie)
#
# opener = urllib.request.build_opener(cookirHandler)
# response = opener.open('http://www.baidu.com')  # type:http.client.HTTPResponse
# # print(type(response))
# # print(response.read().decode('utf-8'))
#
# print(type(cookie))
#
# for item in cookie:
#     print(item)
#     print(item.name+'========'+item.value)
#     print()


# import urllib.request
# import http.cookiejar

# fileName = 'cookies.txt'
# cookie = http.cookiejar.MozillaCookieJar(fileName)
# cookieHandler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(cookieHandler)
#
# response = opener.open('http://www.baidu.com')
# cookie.save(ignore_discard=True, ignore_expires=True)

# import urllib.request
# import http.cookiejar
#
# fileName = 'cookies.txt'
# cookies = http.cookiejar.MozillaCookieJar()
# cookies.load(fileName)
#
# cookieHandler = urllib.request.HTTPCookieProcessor(cookies)
# opener = urllib.request.build_opener(cookieHandler)
# response = opener.open('http://www.baidu.com')
# print(type(response))
# print(response.status)


# import urllib.error
# import urllib.request
#
# try:
#     response = urllib.request.urlopen('http://wpc.iqingcai.com/index.htm')
#     print(type(response))
# except urllib.error.HTTPError as e:
#     print(type(e))
#     print(e.reason, e.url, e.headers, sep='\n')
# except urllib.error.URLError as e:
#     print(type(e))
#     print(e.reason)
# else:
#     print('success')

# import urllib.error
# import urllib.request
# import socket
#
# try:
#     response = urllib.request.urlopen('https://www.baidu.com', timeout=0.01)
# except urllib.error.URLError as e:
#     print(type(e.reason))
#     print(e.reason)
#     if isinstance(e.reason, socket.timeout):
#         print('time out...')

# import urllib.parse
#
# result = urllib.parse.urlparse(url='https://www.baidu.com/index.html#comment', allow_fragments=True)
# print(type(result), result, sep='\n')
#
#
# data = ('http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment')
# print(urllib.parse.urlunparse(data))


# import urllib.parse
#
# params = {
#     'name': 'wangpengchao',
#     'age': 26
# }
#
# baseUrl = 'http://www.baidu.com?'
# url = baseUrl+urllib.parse.urlencode(params)
# print(url)
#
# addParams = urllib.parse.urlencode(params)
# print(addParams)
# print(baseUrl+addParams)
#
#
# print(urllib.parse.parse_qs(addParams)['age'])


# import urllib.parse
#
# keyword = '王鹏超'
# resultUrl = 'http://www.baidu.com/s?wd='+urllib.parse.quote(keyword)
# print(resultUrl)
#
# print(urllib.parse.unquote(resultUrl))

import urllib.robotparser
import urllib.request

rp = urllib.robotparser.RobotFileParser()
rp.set_url('https://blog.csdn.net/robots.txt')
rp.read()

# print(rp.parse(urllib.request.urlopen('http://www.jianshu.com/robots.txt').read().decode('utf-8').split()))
print(rp.can_fetch(useragent='*', url='https://blog.csdn.net/u013088062/article/details/50323393'))

url = 'https://blog.csdn.net/u013088062/article/details/50323393'
response = urllib.request.urlopen(url)
print(response.status)
print(response.read().decode('utf-8'))






