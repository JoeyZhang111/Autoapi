#!/usr/bin/env python  
# encoding: utf-8   
""" 
------------------------
@author: Joey
@file: test_dep.py 
@time: 2021/5/31 10:21 
------------------------
"""

'''
blocker：阻塞缺陷(功能未实现，无法下一步)
critical：严重缺陷(功能点缺失)
normal： 一般缺陷(边界情况，格式错误)
minor：次要缺陷(界面错误与ui需求不符)
trivial： 轻微缺陷(必须项无提示，或者提示不规范)
'''

from Config.conf import conf
from Common.handle_path import data_path,log_path
from api.create_dep import CreateDep
from api.delete_dep import DeleteDep
from Common.get_data import GetData
from Log.get_log import logger
import pytest,os,json
import allure,time
from api.get_token import token
"""
当前写法问题：1、数据问题，每次请求前没有清除原有数据 {1}删数据库 {2}没有权限，调用接口删除原有数据。作为fixture实现
2、每个都获取了token，可以才有pytest的fixture来实现token获取
"""



@allure.feature("部门管理用例")
class TestCreatDep:
    # 读取文件中的用例数据
    path = os.path.join(data_path, conf.get("excel","path"))
    data = GetData(path, conf.get("excel","sheetname1"))
    test_data = data.get_data()

    def setup_class(self):
        logger.info("---新增部门用例开始执行---")

    def teardown_class(self):
        logger.info("---新增部门用例结束执行---")

    @allure.severity("blocker")
    @allure.story("新增部门用例")
    @allure.title("{id}-{name}")
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('id,name,url,method,reqbody,expect',test_data)
    # 执行之前先清除原始数据
    # 调用装饰器，写上测试数据每一列对应的变量名称,然后再写测试数据列表
    def test_create(self,id,name,url,method,reqbody,expect,get_token,del_dep):
        logger.info("执行用例{}{}".format(id,name))
        create = CreateDep()
        body = json.loads(reqbody, strict=False)
        create.send(url=url,method=method,json=body) #根据传进来的测试数据发起不同参数

        #assert
        try:
            # assert res.get("msg") == json.loads(repsData).get("msg")
            expect1 =json.loads(expect)
            assert create.get_res("$.errcode") == json.loads(expect1["errcode"])
        except Exception as e:
            logger.error(f"用例执行失败:{e}")
            raise
        else:
            logger.info("用例执行成功")



@allure.feature("部门管理用例")
class TestDeleteDep:
    # 读取文件中的用例数据
    path = os.path.join(data_path, conf.get("excel", "path"))
    data = GetData(path, conf.get("excel","sheetname2"))
    test_data = data.get_data()

    def setup_class(self):
        logger.info("---删除部门用例开始执行---")

    def teardown_class(self):
        logger.info("---删除部门用例结束执行---")

    @allure.severity("blocker")
    @allure.story("删除部门用例")
    @allure.title("{id}-{name}")
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('id,name,url,method,reqbody,expect', test_data)
    # 执行之前先清除原始数据
    # 调用装饰器，写上测试数据每一列对应的变量名称,然后再写测试数据列表
    def test_delete(self, id,name, url, method, reqbody, expect):
        logger.info("执行用例{} {}".format(id,name))
        create = DeleteDep()
        body = json.loads(reqbody, strict=False)
        body["access_token"] = token

        create.send(url=url, method=method, params=body)  # 根据传进来的测试数据发起不同参数

        # assert
        try:
            expect1 = json.loads(expect)
            assert create.get_res("$.errcode") == expect1["errcode"]
        except Exception as e:
            logger.error(f"用例执行失败:{e}")
            raise
        else:
            logger.info("用例执行成功")

    timer = time.time()
    log_name = os.path.join(log_path, 'excute', f'{timer}.log')
    logger.add(log_name, rotation='100 MB', retention='7 days', enqueue=True, encoding='utf-8')

if __name__ == '__main__':
    pytest.main()


