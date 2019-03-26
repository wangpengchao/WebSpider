# import requests
#
# r = requests.get('http://www.baidu.com')
# print(type(r))
#
# print(r.status_code)
# print(r.text, sep='\n')
# print(r.cookies)

# import requests
#
# r = requests.get(url='http://httpbin.org/get')
# print(type(r.text))
# print(r.text)
# print(r.json())

# import requests
# import re
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:65.0) Gecko/20100101 Firefox/65.0',
# }
# r = requests.get(url='https://www.zhihu.com/explore', headers=headers)
# # print(r.text)
# pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
# titles = re.findall(pattern, r.text)
# titleList = list(titles)
#
# for item in titleList:
#     print(item)

# import requests
#
# r = requests.get(url='https://github.com/favicon.ico')
# with open('favicon.ico', 'wb') as f:
#     f.write(r.content)
#
# print(requests.codes.all_ok)

# import requests
# files = {'file': open('favicon.ico', 'rb')}
# r = requests.post('http://httpbin.org/post', files=files)
# print(r.text)

# import requests
#
# headers = {
#     'Cookie': 'BAIDUID=966C0A6FC48F5386285FF74FAC0FA6F6:FG=1; BIDUPSID=966C0A6FC48F5386285FF74FAC0FA6F6; PSTM=1540045812; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; pgv_pvi=6805171200; BDUSS=hseDdjUERJRlk3MXN2ZW1uZ3R0Z2VlRHdIaUtKfjhKa08yQ0hMeWVwSFMyfkpiQVFBQUFBJCQAAAAAAAAAAAEAAAAsL24rt-i~8UhBRFMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANJOy1vSTstbSG; H_PS_PSSID=; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=1; PSINO=1; BDRCVFR[4r8LXJfwh-6]=I67x6TjHwwYf0; PHPSESSID=amgcqimti0tkj52mkm2g6l8ho5; Hm_lvt_4010fd5075fcfe46a16ec4cb65e02f04=1551252145; Hm_lpvt_4010fd5075fcfe46a16ec4cb65e02f04=1551252145',
#     'Host': 'i.baidu.com',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763',
# }
#
# urlString = 'http://i.baidu.com'
#
# r = requests.get(url=urlString, headers=headers)
# # print(r.text)
# print(type(r.cookies))

# import requests
#
# urlString = 'http://i.baidu.com'
# cookies='BAIDUID=966C0A6FC48F5386285FF74FAC0FA6F6:FG=1; ' \
#         'BIDUPSID=966C0A6FC48F5386285FF74FAC0FA6F6; ' \
#         'PSTM=1540045812; ' \
#         'BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; ' \
#         'pgv_pvi=6805171200; ' \
#         'BDUSS=hseDdjUERJRlk3MXN2ZW1uZ3R0Z2VlRHdIaUtKfjhKa08yQ0hMeWVwSFMyfkpiQVFBQUFBJCQAAAAAAAAAAAEAAAAsL24rt-i~8UhBRFMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANJOy1vSTstbSG; ' \
#         'H_PS_PSSID=; ' \
#         'BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; ' \
#         'delPer=1; ' \
#         'PSINO=1; ' \
#         'BDRCVFR[4r8LXJfwh-6]=I67x6TjHwwYf0; ' \
#         'PHPSESSID=amgcqimti0tkj52mkm2g6l8ho5; ' \
#         'Hm_lvt_4010fd5075fcfe46a16ec4cb65e02f04=1551252145; ' \
#         'Hm_lpvt_4010fd5075fcfe46a16ec4cb65e02f04=1551252145'
#
# cookieJar = requests.cookies.RequestsCookieJar()
# headers = {
#     'Host': 'i.baidu.com',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763',
# }
#
# for cItem in cookies.split(';'):
#     key, value = cItem.split('=', 1)
#     cookieJar.set(key, value)
#
# r = requests.get(url=urlString, cookies=cookieJar, headers=headers)
# print(r.text)


# import requests
#
# s = requests.Session()
# print(type(s))
# s.get('http://httpbin.org/cookies/set/number/12343333')
# r = s.get('http://httpbin.org/cookies')
# print(r.text)


# import requests
# import requests.packages.urllib3
#
# requests.packages.urllib3.disable_warnings()
# response = requests.get(url='https://www.12306.cn', verify=False)
# resultString = response.text.encode('utf-8')
# print(response.status_code)
# print(resultString.decode('utf-8'))


# import requests
# import requests_oauthlib
#
# auth = requests_oauthlib.OAuth1


# import requests
#
# urlString = 'http://httpbin.org/post'
# data = {
#     'name': 'WangPengchao'
# }
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763',
# }
#
# mySession = requests.Session()
# myRequest = requests.Request(method='POST', url=urlString, headers=headers, data=data)
#
# preparedRequest = mySession.prepare_request(myRequest)
#
# response = mySession.send(preparedRequest)
#
# print(response.text)



# import re
#
# content = 'hello 123 4567 world_this is a regex demo'
#
# result = re.match(pattern='^hello\s\d{3}\s\d{4}\s\w{10}', string=content)
#
# print(content.__len__())
# print(result.group().__len__())
# print(result)
# print(result.group())

# import re
# content = 'hello 1234567 world_this is a regex demo'
# result = re.match(pattern='^he.*?(\d+).*demo$', string=content)
# print(result.group(1))


# import re
#
# content = r'extra strings hello 1234567 world_this is a. regex demo extre strings'
# result = re.search('hEllo.*?(\d+).*?demo', content, re.I)
# print(result)
# print(result.group(1))


# import re
#
# html = '''<div id="songs-list">
# <h2 class="title>经典老歌</h2>
# <p class="introduction">
# 经典老歌列表
# </p>
# <ul id="list" class="list-group">
# <li data-view="2">一路上有你</li>
# <li data-view="7">
# <a href ＝"/2.mp3" singer="任贤齐">沧海一声笑</a>
# </li>
# <li data-view="4" class="active">
# <a href ＝"/3.mp3" singer="齐泰">往事随风</a>
# </li>
# <li data-view="6"><a href="/4.mp3" singer="beyond">尤辉岁月</a></li>
# <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
# <li data-view="5">
# <a href="/6.mp3" singer="邓丽君">但愿人长久</a>
# </li>
# </ul>
# </div>'''
#
# result = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>', html, re.S, )
#
# if result:
#     print(result.group(1), result.group(2))


import requests

response = requests.get('http://219.216.96.73/pyxx/Default.aspx')
print(response.text)
