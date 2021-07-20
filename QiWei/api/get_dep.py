#!/usr/bin/env python  
# encoding: utf-8   
""" 
------------------------
@author: Joey
@file: get_dep.py 
@time: 2021/5/31 10:16 
------------------------
"""
from api.base_api import BaseApi
import jsonpath
from api.get_token import GetToken
class GetDep(BaseApi):
    def __init__(self):
        # 先实现父类的初始化函数
        BaseApi.__init__(self)
        self.url = self.host + "/cgi-bin/department/list"
        self.method = "get"
        # params参数存放要认证的token字段，值动态变化
        self.params = {
            "access_token": BaseApi.token
        }
if __name__ == '__main__':
    get = GetDep()
    r = get.send()
    print(r.json())
    # list = jsonpath.jsonpath(r.json(),"$..id")
    # for i in list:
    #     print(i)

