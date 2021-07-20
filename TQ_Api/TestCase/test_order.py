#!/usr/bin/env python  
# encoding: utf-8   
""" 
------------------------
@author: Joey
@file: test_order.py 
@time: 2021/6/30 16:18 
------------------------
"""
import allure,pytest,os,json,random
from Common.base_dir import data_path
from Conf.read_conf import ini
from Common.get_excel import GetData
from Api.base_api import BaseApi
from Api.DirectOrder import GetDirect
from Api.CardOrder import Card
from Api.credit import Credit



# 当一个函数被声明为夹具的时候，可以在测试函数中传入这个夹具的名称，pytest 会自动调用它
# 如果不写参数，参数就是scope="function"，它的作用范围是每个测试用例来之前运行一次，销毁代码在测试用例之后运行。
@pytest.fixture()
def randomnum():
    num = str(random.randint(1111111111, 9999999999))
    return num

@allure.feature("订单管理用例")
class TestDirectOrder:
    # 读取文件中的用例数据
    path = os.path.join(data_path, ini.get("excel","path1"))
    data = GetData(path, ini.get("excel","sheetname1"))
    test_data = data.get_data()

    def setup_class(self):
        BaseApi.logger.info("---直充订单用例开始执行---")

    def teardown_class(self):
        BaseApi.logger.info("---直充订单用例结束执行---")

    @allure.severity("blocker")
    @allure.story("直充订单用例")
    @allure.title("{id}-{name}")
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('id,name,url,method,reqbody,respdata',test_data)
    # 执行之前先清除原始数据
    # 调用装饰器，写上测试数据每一列对应的变量名称,然后再写测试数据列表
    def test_direct(self,id,name,url,method,reqbody,respdata,randomnum):
        BaseApi.logger.info("执行用例{}{}".format(id,name))
        newurl = ini.get("url","host1") + url
        direct = GetDirect()
        header = {'Content-Type':'application/x-www-form-urlencoded'}
        body = json.loads(reqbody,strict=False)
        body["TimesTamp"] = str(BaseApi().time_stamp())
        body["MOrderID"] = randomnum
        newsign = body["AppKey"] + body["BuyCount"] + body["CallBackUrl"] + body["ChargeAccount"] + body["CustomerIP"] + body["MOrderID"] + body["ProductCode"] + body["TimesTamp"] + body["Version"] + body["AppSecret"]
        body["Sign"] = BaseApi.get_md5(newsign)

        direct.get(url=newurl,method=method,data=body,headers=header) #根据传进来的测试数据发起不同参数

        #assert
        try:
            # assert res.get("msg") == json.loads(repsData).get("msg")
            expect = json.loads(respdata)
            assert direct.get_res("$.Msg") == expect["Msg"]

        except Exception as e:
            BaseApi.logger.error(f"用例执行失败:{e}")
            raise
        else:
            BaseApi.logger.info("用例执行成功")

@allure.feature("订单管理用例")
class TestCardOrder:
    # 读取文件中的用例数据
    path = os.path.join(data_path, ini.get("excel","path1"))
    data = GetData(path, ini.get("excel","sheetname2"))
    test_data = data.get_data()

    def setup_class(self):
        BaseApi.logger.info("---卡密订单用例开始执行---")

    def teardown_class(self):
        BaseApi.logger.info("---卡密订单用例结束执行---")

    @allure.severity("blocker")
    @allure.story("卡密订单用例")
    @allure.title("{id}-{name}")
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('id,name,url,method,reqbody,respdata',test_data)
    # 执行之前先清除原始数据
    # 调用装饰器，写上测试数据每一列对应的变量名称,然后再写测试数据列表
    def test_Order(self,id,name,url,method,reqbody,respdata,randomnum):
        BaseApi.logger.info("执行用例{}{}".format(id,name))
        newurl = ini.get("url", "host1") + url
        card = Card()
        header = {'Content-Type':'application/x-www-form-urlencoded'}
        body = json.loads(reqbody,strict=False)
        body["TimesTamp"] = str(BaseApi().time_stamp())
        body["MOrderID"] = randomnum
        newsign = body["AppKey"] + body["BuyCount"] + body["CallBackUrl"] + body["ChargeAccount"] + body["CustomerIP"] + body["MOrderID"] + body["ProductCode"] + body["TimesTamp"] + body["Version"] + body["AppSecret"]
        body["Sign"] = BaseApi.get_md5(newsign)

        card.get(url=newurl,method=method,data=body,headers=header) #根据传进来的测试数据发起不同参数

        #assert
        try:
            # assert res.get("msg") == json.loads(repsData).get("msg")
            expect = json.loads(respdata)
            assert card.get_res("$.Msg") == expect["Msg"]

        except Exception as e:
            BaseApi.logger.error(f"用例执行失败:{e}")
            raise
        else:
            BaseApi.logger.info("用例执行成功")

@allure.feature("话费管理用例")
class TestCredit:
    # 读取文件中的用例数据
    path = os.path.join(data_path, ini.get("excel","path2"))
    data = GetData(path, ini.get("excel","sheetname3"))
    test_data = data.get_data()

    def setup_class(self):
        BaseApi.logger.info("---话费订单用例开始执行---")

    def teardown_class(self):
        BaseApi.logger.info("---话费订单用例结束执行---")

    @allure.severity("blocker")
    @allure.story("话费订单用例")
    @allure.title("{id}-{name}")
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize('id,name,url,method,reqbody,respdata',test_data)
    # 执行之前先清除原始数据
    # 调用装饰器，写上测试数据每一列对应的变量名称,然后再写测试数据列表
    def test_credit(self,id,name,url,method,reqbody,respdata,randomnum):
        BaseApi.logger.info("执行用例{}{}".format(id,name))
        newurl = ini.get("url","host2") + url
        credit = Credit()
        body = json.loads(reqbody,strict=False)
        body["TimesTamp"] = str(BaseApi().now_time())
        body["MOrderID"] = randomnum
        newsign = body["ApiAccount"] + body["MOrderID"] + body["ProductCode"] + body["ChargeNum"] + body["Quantity"] + body["TimesTamp"] + body["ApiKey"]
        body["Sign"] = BaseApi.get_md5(newsign)
        credit.get(url=newurl,method=method,json=body) #根据传进来的测试数据发起不同参数

        #assert
        try:
            # assert res.get("msg") == json.loads(repsData).get("msg")
            expect = json.loads(respdata)
            assert credit.get_res("$.Response.ResponseMessage") == expect["Response"]["ResponseMessage"]

        except Exception as e:
            BaseApi.logger.error(f"用例执行失败:{e}")
            raise
        else:
            BaseApi.logger.info("用例执行成功")





"""
if __name__ == '__main__':
    pytest.main()
    """

