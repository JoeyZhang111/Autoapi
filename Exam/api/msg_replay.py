#!/usr/bin/env python  
# encoding: utf-8   
""" 
------------------------
@author: Joey
@file: mag_replay.py 
@time: 2021/7/16 16:20 
------------------------
"""
from api.base_api import BaseApi
from conf.get_conf import ini


class Replay(BaseApi):
    def __init__(self):
        BaseApi.__init__(self)
        self.url = ini.get("url","host") + "/api/replay"
        self.method = "post"
        self.headers = {
            "X-AUTH-TOKEN": BaseApi.token,
            "Content-Type": "application/json"
        }
        self.json = {
            "replay": "个准确的定义",
            "messageId": "1"
        }


rep = Replay()
print(rep.send().json())
