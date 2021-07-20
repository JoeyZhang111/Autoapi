#!/usr/bin/env python  
# encoding: utf-8   
""" 
------------------------
@author: Joey
@file: test_add.py 
@time: 2021/7/20 14:31 
------------------------
"""
from api.msg_add import Add
import pytest,os,allure,json
from api.base_api import BaseApi
from conf.get_conf import ini
from common.base_dir import data_path
from conf.get_conf import ini
from common.read_data import GetData
@allure.feature("留言板块用例")
class TestAdd:
    # 读取文件中的用例数据
    path = os.path.join(data_path, ini.get("excel", "path"))
    data = GetData(path, ini.get("excel", "sheetname2"))
    testdata = data.get_data()

    def setup_class(self):
        print("----------新增留言开始------------")
    def teardown_class(self):
        print("----------新增留言结束------------")

    @allure.severity("blocker")
    @allure.story("新增留言用例")
    @allure.title("{id}-{name}")
    @pytest.mark.parametrize("id,name,url,method,body,res",testdata)
    def test_add(self,id,name,url,method,body,res,get_token):
        BaseApi.logger.info("执行用例{}{}".format(id,name))
        newurl = ini.get("url","host") + url
        add = Add()
        newbody = json.loads(body)
        add.send(url=newurl,method=method,json=newbody)

        try:
            expect =  json.loads(res)
            assert add.get_res("$.message") == expect["message"]
        except Exception as e:
            BaseApi.logger.error(f"用例执行失败:{e}")
            raise
        else:
            BaseApi.logger.info("用例执行成功")

"""
if __name__ == '__main__':
    pytest.main(["-sv","test_login.py"])
"""