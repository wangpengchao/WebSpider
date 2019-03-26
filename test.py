# import requests
# from selenium import webdriver

# r = requests.get(url='https://www.amazon.cn/dp/B00RRDKWN8/ref=cngwdyfloorv2_recs_0?pf_rd_p=d0690322-dfc8-4e93-ac2c-8e2eeacbc49e&pf_rd_s=desktop-2&pf_rd_t=36701&pf_rd_i=desktop&pf_rd_m=A1AJ19PSB66TGU&pf_rd_r=428MR48D5Y817R0JSZS5&pf_rd_r=428MR48D5Y817R0JSZS5&pf_rd_p=d0690322-dfc8-4e93-ac2c-8e2eeacbc49e')
# driver = webdriver.Chrome()
# driver.get('https://weibo.com/')
# driver.get('http://www.baidu.com')
# print(driver.page_source)


# def fmap(a,b):
#     return (a+1, b+'z')
#
# keys = range(1, 11)
# values = list('qazxswedcvf')
# result = map(fmap, keys, values)
# r = dict(result)
# print(r)


# keys = range(11, 21)
# values = list('qazxswedcvf')
# r = zip(keys, values)
# d = dict(r)
# print(d)

# class Sample:
#     def __enter__(self):
#         print('In __enter__()')
#         return 'Foo'
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('In __exit__()')
#
# def getSample():
#     return Sample()
#
# with getSample() as sm:
#     print('sample: ' + sm)


# class Sample:
#     def __enter__(self):
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('exc_type ' + str(exc_type))
#         print('exc_val ' + str(exc_val))
#         print('exc_tb ' + str(exc_tb))
#
#     def doSomthing(self):
#         return 1/0
#
#
# with Sample() as sm:
#     sm.doSomthing()


# class DummyResource:
#     def __init__(self, tag):
#         self.tag = tag
#         print('Resource [%s]' % tag)
#
#     def __enter__(self):
#         print('[Enter %s]: 分配资源.' % self.tag)
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('[Exit %s]: 释放资源' % self.tag)
#
#         if exc_tb is None:
#             print('[Exit %s]: 无异常退出.' % self.tag)
#         else:
#             print('[Exit %s]: 退出时发生异常' % self.tag)
#             return False
#
#
# with DummyResource('Normal'):
#     print('[with-body] run without exceptions.')
#
# print('开始下一个')
#
# with DummyResource('with-exception'):
#     print('[with-body] run with exception.')
#     raise Exception
#     print('[with-body] Run with exception. Failed to finish statement-body!')


import http.client
import http.cookiejar


import urllib.error
import urllib.parse
import urllib.robotparser

import requests.sessions

import urllib3



