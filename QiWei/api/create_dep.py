#!/usr/bin/env python  
# encoding: utf-8   
""" 
------------------------
@author: Joey
@file: create_dep.py 
@time: 2021/5/28 15:13 
------------------------
"""
from api.get_token import token
from api.base_api import BaseApi
class CreateDep(BaseApi):
    def __init__(self):
        # 先实现父类的初始化函数
        BaseApi.__init__(self)
        self.url = self.host + "/cgi-bin/department/create"
        self.method = "post"
        # params参数存放要认证的token字段，值动态变化
        self.params ={
            "access_token":BaseApi.token
        }
        self.json = {
            "name": "技术部",
            "name_en": "JSB",
            "parentid": 1,
            "order": 1,
            "id": 5
            }
if __name__ == '__main__':
    pass
    """
    BaseApi.token = token
    create = CreateDep()
    dep = create.send()
    print(create.get_res("$.errcode"))
    """

