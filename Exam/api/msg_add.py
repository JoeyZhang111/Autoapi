#!/usr/bin/env python  
# encoding: utf-8   
""" 
------------------------
@author: Joey
@file: msg_add.py
@time: 2021/7/16 14:37 
------------------------
"""
from api.base_api import BaseApi
from conf.get_conf import ini


class Add(BaseApi):
    def __init__(self):
        BaseApi.__init__(self)
        self.url = ini.get("url","host") + "/api/message"
        self.method = "post"
        self.headers = {
            "X-AUTH-TOKEN": BaseApi.token,
            "Content-Type": "application/json"
        }
        self.json = {
            "title":"分的高分经典回顾符合国家和的结果功兑高度风格化的风反对恢复供电和大家思考的风格格关于个环人约特如图杠代光华",
            "content":"留言内容"
        }

"""
msg = Add()
m = msg.send()
print(m.json())"""