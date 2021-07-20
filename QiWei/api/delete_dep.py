#!/usr/bin/env python  
# encoding: utf-8   
""" 
------------------------
@author: Joey
@file: delete_dep.py 
@time: 2021/5/28 15:25 
------------------------
"""
from api.get_token import token
from api.base_api import BaseApi
class DeleteDep(BaseApi):
    def __init__(self):
        # 先实现父类的初始化函数
        BaseApi.__init__(self)
        self.url = self.host + "/cgi-bin/department/delete"
        self.method = "get"
        # params参数存放要认证的token字段，值动态变化
        self.params = {
            "access_token": BaseApi.token,
            "id":"2"
        }
if __name__ == '__main__':
    # print(BaseApi.token )
    """
    import json
    BaseApi.token = token
    dele = DeleteDep()
    de = dele.send()
    a = de.text
    b = json.loads(a)
    print(b["errcode"])
    """
    pass

