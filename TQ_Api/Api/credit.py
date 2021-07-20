#!/usr/bin/env python  
# encoding: utf-8   
""" 
------------------------
@author: Joey
@file: credit.py 
@time: 2021/7/6 16:34 
------------------------
"""
import time,hashlib
from Conf.read_conf import ini
from Api.base_api import BaseApi



class Credit(BaseApi):
    def __init__(self):
        BaseApi.__init__(self)
        self.method = "post"
        host = ini.get("url","host2")
        self.url = host + "/SubmitOrder.ashx"
        print(self.url)
        newdata = {
            "ApiAccount": "TestApi",
            "MOrderID": str(BaseApi().time_stamp()),
            "ProductCode": "AHW_YD_01_002000_0001",
            "ChargeNum": "18884178456",
            "Quantity": "1",
            "TimesTamp": str(BaseApi().now_time())

        }
        params = { "ApiKey": "A3CD52180AF4EC928465B45FEF15E268"}
        sign = newdata["ApiAccount"] + newdata["MOrderID"] + newdata["ProductCode"] + newdata["ChargeNum"] +newdata["Quantity"] + newdata["TimesTamp"] +params["ApiKey"]
        newdata["Sign"] = BaseApi.get_md5(sign)
        self.json = newdata
        print(self.json)


order = Credit()
print(order)
o = order.get()
print(o.text)
