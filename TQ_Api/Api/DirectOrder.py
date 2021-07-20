#!/usr/bin/env python  
# encoding: utf-8   
""" 
------------------------
@author: Joey
@file: DirectOrder.py 
@time: 2021/6/18 9:27 
------------------------
"""
from Conf.read_conf import ini
from Api.base_api import BaseApi


class GetDirect(BaseApi):
    def __init__(self):
        # 先实现父类的初始化函数
        BaseApi.__init__(self)

        self.url = ini.get("url","host1") + "/Order/DirectOrder"
        self.method = "get"
        self.headers = {"Content-Type": "application/x-www-form-urlencoded"}
        newdata = {
            "AppKey": "211394680",
            "TimesTamp": str(BaseApi().time_stamp()),
            "ProductCode": "PLM100032",
            "BuyCount": "1",
            "MOrderID": str(BaseApi().time_stamp()),
            "ChargeAccount": "18884178456",
            "ChargeAccountType": "1",
            "CustomerIP": "121.43.39.80",
            "Version": "1.0",
            "IsCallback":"1",
            "CallBackUrl": "http://192.168.0.198:8033/CallBack/Test",
            "AppSecret": "lOqVb8XGUkm1O/ppIxKhsg=="
        }
        newsign = newdata["AppKey"] + newdata["BuyCount"] + newdata["CallBackUrl"] + newdata["ChargeAccount"] + newdata["CustomerIP"] + newdata["MOrderID"] + newdata["ProductCode"] + newdata["TimesTamp"] + newdata["Version"] + newdata["AppSecret"]
        newdata["Sign"] = BaseApi.get_md5(newsign)
        self.data = newdata
        print(self.data)

        # print(newdata)

get_order = GetDirect()
order = get_order.get()

if __name__ == '__main__':
    pass
"""
    get_order = GetDirect()
    order = get_order.get()
    o = get_order.get_res("$.Code")
    print(o)
    """




