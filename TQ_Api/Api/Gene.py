#!/usr/bin/env python  
# encoding: utf-8   
""" 
------------------------
@author: Joey
@file: Generate.py 
@time: 2021/7/7 11:41 
------------------------
"""
from Api.base_api import BaseApi
from Conf.read_conf import ini
class Gene(BaseApi):
    def __init__(self):
        BaseApi.__init__(self)
        self.url = ini.get("url","host3") + "/Service/Generate"
        self.method = "post"
        payload = {
            "DomainName": "192.168.0.46:8097",
            "Url":"http://www.baodusaohu.com",
            "Token":"8630828582824b0e9e4b8bb72da3fc53",
            "validity":"2020-10-10 10:10:10",
            "timestamp":BaseApi().time(),
            "Account" : "14545245123"
            }

        sign = payload["DomainName"] +payload["Url"] + payload["Token"] + payload["validity"] + payload["timestamp"]+ payload["Account"]
        newsign = BaseApi.get_md5(sign)
        payload["Sign"] = newsign

        self.json = payload
        # print(self.json)


gene = Gene()
g = gene.get()
print(g.json())



