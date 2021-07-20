#!/usr/bin/env python  
# encoding: utf-8   
""" 
------------------------
@author: Joey
@file: login.py
@time: 2021/7/5 16:27 
------------------------
"""
from api.base_api import BaseApi
from conf.get_conf import ini

class Login(BaseApi):
    def __init__(self):
        BaseApi.__init__(self)
        self.url = ini.get("url","host")+"/api/loginS"
        self.method = "post"
        payload = {"username": "20154084","password": "123456"}
        payload["password"] = BaseApi.get_md5(payload["password"])
        self.json = payload

"""
get = Login()
get.send()
tokens = get.get_res("$.message")
"""


