#!/usr/bin/env python  
# encoding: utf-8   
""" 
------------------------
@author: Joey
@file: conftest.py 
@time: 2021/5/31 10:32 
------------------------
"""
import pytest
from api.base_api import BaseApi
from api.get_token import GetToken
from api.get_dep import GetDep
from api.delete_dep import DeleteDep
#范围session指每次执行开始就去请求token
@pytest.fixture(scope="class",autouse=True)
def get_token():
    get_token = GetToken()
    get_token.send()
    BaseApi.token = get_token.get_res('$.access_token')

@pytest.fixture(scope="class")
def del_dep():
#     调用删除接口，如何获取id? 先调获取列表得到id
    get = GetDep()
    get.send()
    list_id = get.get_res_all("$..id")
    delete = DeleteDep()
    # 遍历所有的id，一一删除
    for i in list_id:
        delete.params["id"] = i
        delete.send()