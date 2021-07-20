#!/usr/bin/env python  
# encoding: utf-8   
""" 
------------------------
@author: Joey
@file: msg_list.py 
@time: 2021/7/16 16:51 
------------------------
"""
from api.base_api import BaseApi
from conf.get_conf import ini

class List(BaseApi):
    def __init__(self):
        BaseApi.__init__(self)
        page = "y"
        value = "4"
        self.url = ini.get("url","host") + "/api/messages/" + page + "/" + value
        self.method = "get"
        self.headers = {"X-AUTH-TOKEN": BaseApi.token}

"""
rep = List()
print(rep.send().json())
"""


