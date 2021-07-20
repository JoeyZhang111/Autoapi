#!/usr/bin/env python  
# encoding: utf-8   
""" 
------------------------
@author: Joey
@file: client.py 
@time: 2021/7/5 15:35 
------------------------
"""
import requests
class RequestClient:
    def __init__(self):
        # seesion()对象发出的所有请求之间保持cookie信息,requests则需要在响应中获取cookies带入下个请求
        self.session = requests.session()

    # request代表请求方式get/post,return后面调用才会返回非None
    def send(self,**kwargs):
        return self.session.request(**kwargs)
