#!/usr/bin/env python  
# encoding: utf-8   
""" 
------------------------
@author: Joey
@file: Exchange.py 
@time: 2021/7/9 15:12 
------------------------
"""
from Api.base_api import BaseApi
from Conf.read_conf import ini
class Exchange(BaseApi):
    def __init__(self):
        BaseApi.__init__(self)
        self.url = ini.get("url","host4") + "/ExtractPointCards/getcodedata"
        self.method = "post"
        payload = {
            "merchant_id":"600000038253",
            "mobile":"18888888888",
            "sub_order_id":BaseApi().now_time(),
            "ext_goods_id": "17",
            "buy_num":"1",
            "expire_time":"2021-11-23 15:00:00",
            "start_time":"2020-11-22 15:00:00",
            "sign":"123"
        }

        self.json = payload

if __name__ == '__main__':
    ex = Exchange()
    print(ex.get().json())