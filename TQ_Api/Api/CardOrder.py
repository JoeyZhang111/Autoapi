#!/usr/bin/env python  
# encoding: utf-8   
""" 
------------------------
@author: Joey
@file: CardOrder.py 
@time: 2021/6/21 16:59 
------------------------
"""
import time,hashlib
from Conf.read_conf import ini
from Api.base_api import BaseApi


class Card(BaseApi):
    def __init__(self):
        BaseApi.__init__(self)

        self.method = "post"
        host = ini.get("url","host1")
        self.url = host + "/Order/CardOrder"
        self.headers  = {"Content-Type": "application/x-www-form-urlencoded"}
        data = {
            "AppKey": "211394680",
            "TimesTamp": str(BaseApi().time_stamp()),
            "ProductCode": "PLM10032",
            "BuyCount": "1",
            "MOrderID": str(BaseApi().time_stamp()),
            "ChargeAccount": "1756643654",
            "ChargeAccountType": "1",
            "CustomerIP": "123.123.123.123",
            "Version": "1.0",
            "AppSecret": "lOqVb8XGUkm1O/ppIxKhsg==",
            "PublicKey": "-----BEGIN PUBLIC KEY-----MIIBIDANBgkqhkiG9w0BAQEFAAOCAQ0AMIIBCAKCAQEAq3XfgBSkaOYtESoE9nxyIB/fhCbn7EGLt0FtLqk9Dww4k/tFBCPP0hxr7xXb21VOLIER4+npcyBGaHXmnp3fGLKGN6s014MQOyCl6P2JFT/iWC1cp6GKSlIMmK1oaNBpcB11xvWa4fCg9E10JgdNBT9G0syxezJn0iIJkE4IxLfV3RciQtYnv7D3TcY38jzKmOcT9sbyWyPNI7UWIvSNMzmu/5Xev2Q4ZKcnlNePIg7aPHQmYp8YekEzRabRnwHfdhjpQI0Hr7YIa6+qsUpmPtEx4jVsJ607VmehfGnnapmrWk0c7iqxhAADARJFLKW97TCUtc6qB5NXvmoXckw0MQIBAw==-----END PUBLIC KEY-----"
        }
        sign = data["AppKey"] + data["BuyCount"] + data["ChargeAccount"] + data["CustomerIP"] + data["MOrderID"] + data["ProductCode"] + data["TimesTamp"] + data["Version"] + data["AppSecret"]
        data["Sign"] = BaseApi.get_md5(sign)
        self.data = data

get_order = Card()
order = get_order.get()
# res = order.get_res()
# print(res)