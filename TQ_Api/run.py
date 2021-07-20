#!/usr/bin/env python  
# encoding: utf-8   
""" 
------------------------
@author: Joey
@file: run.py 
@time: 2021/6/30 17:49 
------------------------
"""
import pytest,os
if __name__ == '__main__':
    pytest.main()
    # 想要自动生成报告，还要安装allure指令行
    os.system("allure generate ../Report/Or -o ./Report/html --clean")
    os.system("allure serve ../Report/Or")