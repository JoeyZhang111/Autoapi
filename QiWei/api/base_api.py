#!/usr/bin/env python  
# encoding: utf-8   
""" 
------------------------
@author: Joey
@file: base_api.py 
@time: 2021/5/26 14:50 
------------------------
"""
import requests
from Common.client import RequestClient
import jsonpath
class BaseApi:
#     设置一个全局变量token
    token = None
#baseapi作为所有单接口的父类，将所有接口公共的属性或方法信息抽象封装
    def __init__(self):
        #发起请求的客户端对象
        self.client = RequestClient()
        self.host = "https://qyapi.weixin.qq.com"
        self.url = None
        self.method = None
        self.headers = None
        self.data = None
        self.params = None
        self.json = None
        self.res = None

    def send(self,**kwargs): #**kwargs,接口发起时有一些自定义参数
        #表示调用方如果不传递某个字段，就把当前对象的请求（self.url=None）赋值给它

        if kwargs.get('method') == None:
            kwargs["method"] = self.method
        if kwargs.get('url') == None:
            kwargs["url"] = self.url
        if kwargs.get('headers') == None:
            kwargs["headers"] = self.headers
        if kwargs.get('data') == None:
            kwargs["data"] = self.data
        if kwargs.get('params') == None:
            kwargs["params"] = self.params
        if kwargs.get('json') == None:
            kwargs["json"] = self.json

        # 调用client进行发起

        self.res = self.client.send(**kwargs)
        return self.res

#         对于每一个接口，都有可能提取响应中的某个字段的值
#         在父类里面封装响应值,
#   提取第一个响应
    def get_res(self,jsonpath_express):
        return jsonpath.jsonpath(self.res.json(),jsonpath_express)[0]
#   提取所有响应
    def get_res_all(self,jsonpath_express):
        return jsonpath.jsonpath(self.res.json(), jsonpath_express)



