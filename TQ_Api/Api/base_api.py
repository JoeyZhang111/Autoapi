#!/usr/bin/env python  
# encoding: utf-8   
""" 
------------------------
@author: Joey
@file: base_api.py 
@time: 2021/6/11 11:44 
------------------------
"""

from Common.client import RequestClient
import jsonpath,datetime
import hashlib,time
from Log.get_log import Logger
class BaseApi:
    # 创建日志对象为全局变量
    logger = Logger()

    def __init__(self):
        # baseapi作为所有单接口的父类，将所有接口公共的属性或方法信息抽象封装
        self.client = RequestClient()
        self.url = None
        self.method = None
        self.headers = None
        self.params = None
        self.data = None
        self.json = None
        self.res = None

    def get(self,**kwargs): #**kwargs,接口发起时有一些自定义参数
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

    # 提取第一个响应
    def get_res(self,jsonpath_express):
        return jsonpath.jsonpath(self.res.json(), jsonpath_express)[0]

    # 提取所有响应
    def get_res_all(self, jsonpath_express):
        return jsonpath.jsonpath(self.res.json(), jsonpath_express)

    # 定义MD5加密签名
    def get_md5(sign):
        # 创建MD5对象
        md5 = hashlib.md5()
        # 加密方法
        md5.update(f'{sign}'.encode(encoding='UTF-8'))
        # 得到加密后结果
        md = md5.hexdigest().upper()
        return md

    #定义时间戳
    def time_stamp(self):
        timer = time.time()
        tim = int(round(timer)*1000)
        return tim

    # 定义系统时间yyyymmddhhMMss
    def now_time(self):
        now_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        return now_time

    def time(self):
        t = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return  t










