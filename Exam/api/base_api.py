#!/usr/bin/env python  
# encoding: utf-8   
""" 
------------------------
@author: Joey
@file: BaseApi.py
@time: 2021/7/5 15:31 
------------------------
"""
from common.client import RequestClient
import jsonpath,hashlib
from log.get_log import Logger
class BaseApi:
    # 全局变量log
    logger = Logger()
    # 全局变量token
    token = None

    #baseapi作为所有单接口的父类，将所有接口公共的属性或方法信息抽象封装
    def __init__(self):
        #初始化参数为空
        self.client =RequestClient()
        self.url = None
        self.method = None
        self.headers = None
        self.params = None
        self.data = None
        self.json = None
        self.res = None

    def send(self,**kwargs):
        # 如果在传参过程中传某参数没有赋值，则传入self.xxx = None
        if kwargs.get("url") == None:
            kwargs["url"] = self.url
        if kwargs.get("method") == None:
            kwargs["method"] = self.method
        if kwargs.get("headers") == None:
            kwargs["headers"] = self.headers
        if kwargs.get("params") == None:
            kwargs["params"] = self.params
        if kwargs.get("data") == None:
            kwargs["data"] = self.data
        if kwargs.get("json") == None:
            kwargs["json"] = self.json

        self.res = self.client.send(**kwargs)
        return self.res

    def get_res(self,jsonpath_express):
        return jsonpath.jsonpath(self.res.json(),jsonpath_express)[0]

    # 定义MD5加密签名
    def get_md5(pwd):
        # 创建MD5对象
        md5 = hashlib.md5()
        # 加密方法
        md5.update(f'{pwd}'.encode('utf-8'))
        # 得到加密后结果
        md = md5.hexdigest()
        return md
