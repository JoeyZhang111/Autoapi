#!/usr/bin/env python  
# encoding: utf-8   
""" 
------------------------
@author: Joey
@file: msg_del.py 
@time: 2021/7/16 17:21 
------------------------
"""
from api.base_api import BaseApi
from conf.get_conf import ini


class Del(BaseApi):
    def __init__(self):
        BaseApi.__init__(self)
        id = "y"
        self.url = ini.get("url","host") + "/api/message/" +id
        self.method = "delete"
        self.headers = {"X-AUTH-TOKEN": BaseApi.token,"Content-Type":"application/json;charset=UTF-8"}


rep = Del()
print(rep.send().json())
