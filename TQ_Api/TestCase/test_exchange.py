#!/usr/bin/env python  
# encoding: utf-8   
""" 
------------------------
@author: Joey
@file: test_exchange.py 
@time: 2021/7/9 15:20 
------------------------
"""
from Conf.read_conf import ini
from Api.base_api import BaseApi
from Common.get_excel import GetData
import os,allure,pytest,json
from Api.Exchange import Exchange
from Common.base_dir import data_path
@allure.feature("短链接生成管理用例")
class TestGene:
    # 读取文件中的用例数据
    path = os.path.join(data_path, ini.get("excel","path4"))
    data = GetData(path, ini.get("excel","sheetname5"))
    test_data = data.get_data()

    def setup_class(self):
        BaseApi.logger.info("---积分卡提取用例开始执行---")

    def teardown_class(self):
        BaseApi.logger.info("---积分卡提取用例结束执行---")

    @allure.severity("blocker")
    @allure.story("积分卡提取订单用例")
    @allure.title("{id}-{name}")
    @pytest.mark.run(order=4)
    @pytest.mark.parametrize('id,name,url,method,reqbody,respdata',test_data)
    # 执行之前先清除原始数据
    # 调用装饰器，写上测试数据每一列对应的变量名称,然后再写测试数据列表
    def test_gene(self,id,name,url,method,reqbody,respdata):
        BaseApi.logger.info("执行用例{}{}".format(id,name))
        newurl = ini.get("url","host4") + url
        ex = Exchange()
        body = json.loads(reqbody,strict=False)
        body["sub_order_id"] = str(BaseApi().now_time())

        ex.get(url=newurl,method=method,json=body) #根据传进来的测试数据发起不同参数


        try:
            expect = json.loads(respdata)

            assert ex.get_res("$.resp_desc") == expect["resp_desc"]

        except Exception as e:
            BaseApi.logger.error(f"用例执行失败:{e}")
            raise
        else:
            BaseApi.logger.info("用例执行成功")

"""
if __name__ == '__main__':
    pytest.main(["-sv","test_exchange.py"])
"""