import requests


# payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
# r = requests.get('http://api.github.com/get',
#                  params=payload)
# print(r.url)

# r = requests.get('https://api.github.com/events', stream=True)
# print(r.ra)

# url = 'https://api.github.com/some/endpoint'
# headers = {'user-agent': 'my-app/0.0.1'}
# r = requests.get(url, headers=headers)
# print(r.text)
# re = requests.get(url)
# print(re.text)

# payload = {'key1': 'value1', 'key2': 'value2'}
# myURL = 'http://httpbin.org/post'
# r = requests.post(url=myURL, data=payload)
# print(r.text)
from asn1crypto.x509 import PrintableAddress

# r = requests.get('http://httpbin.org/get')
# print(r.status_code)
# print(r.headers)
# print(r.headers['server'])
# print(r.headers.get('Server'))

# url = 'http://httpbin.org/cookies'
# cookies = dict(myCookies='myWorking', yourcookies='yourWorking')  # 使用函数的方式生成字典
# cookies2 = {'myCookies': 'myWorking', 'yourcookies': 'yourWorking'}  # 直接传入字典
#
# r = requests.get(url=url, cookies=cookies2)
# print(type(r.cookies))
# print(r.text)

jar = requests.cookies.RequestsCookieJar()  # 定义一个cookies类
jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
jar.set('gross_cookie', 'blech', domain='httpbin.org', path='/elsewhere')
url = 'http://httpbin.org/cookies'
r = requests.get(url=url, cookies=jar)
print(r.text)

