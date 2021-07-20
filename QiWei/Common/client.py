#!/usr/bin/env python  
# encoding: utf-8   
""" 
------------------------
@author: Joey
@file: client.py 
@time: 2021/5/28 13:49 
------------------------
"""
import requests
#封装发起请求的客户端对象
class RequestClient():

    def __init__(self):
        # seesion()对象发出的所有请求之间保持cookie信息,requests则需要在响应中获取cookies带入下个请求
        self.session = requests.session()
    def send(self,**kwargs):
        #发起请求
        return self.session.request(**kwargs)

"""

# 登陆接口
response1 = requests.get(url_login,params,headers)
# 获取cookies信息
cookies = response.cookies
# 得到的cookies 是一个字典类型
cookie = cookies.get("cookies的key")
# 请求 查询接口
response2 = requests.get(search_url,params,headers,cookies=cookie)
# 查看查询响应的结果
response2.json()
----------------------------------------------------------------
# 获取 session对象
session = requests.session()
# 登陆接口
response1 = session.get(url_login,params,headers)
# 请求 查询接口
response2 = session.get(search_url,params,headers)
# 查看查询响应的结果
response2.json()
"""


