#!/usr/bin/env python  
# encoding: utf-8   
""" 
------------------------
@author: Joey
@file: test_login.py 
@time: 2021/7/19 11:15 
------------------------
"""
from api.login import Login
import pytest,os,allure,json
from api.base_api import BaseApi
from conf.get_conf import ini
from common.base_dir import data_path
from conf.get_conf import ini
from common.read_data import GetData
@allure.feature("登录用例")
class TestLogin:
    # 读取文件中的用例数据
    path = os.path.join(data_path, ini.get("excel", "path"))
    data = GetData(path, ini.get("excel", "sheetname1"))
    testdata = data.get_data()

    def setup_class(self):
        print("----------登录用例开始------------")
    def teardown_class(self):
        print("----------结束用例开始------------")

    @allure.severity("blocker")
    @allure.story("登录用例")
    @allure.title("{id}-{name}")
    @pytest.mark.parametrize("id,name,url,method,body,res",testdata)
    def test_login(self,id,name,url,method,body,res):
        BaseApi.logger.info("执行用例{}{}".format(id,name))
        newurl = ini.get("url","host") + url
        login = Login()
        newbody = json.loads(body)
        newbody["password"] = BaseApi.get_md5(newbody["password"])
        login.send(url=newurl,method=method,json=newbody)

        try:
            expect =  json.loads(res)
            assert login.get_res("$.message") == expect["message"]
        except Exception as e:
            BaseApi.logger.error(f"用例执行失败:{e}")
            raise
        else:
            BaseApi.logger.info("用例执行成功")

"""
if __name__ == '__main__':
    pytest.main(["-sv","test_login.py"])
"""

