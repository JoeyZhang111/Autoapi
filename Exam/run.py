#!/usr/bin/env python  
# encoding: utf-8   
""" 
------------------------
@author: Joey
@file: run.py 
@time: 2021/7/19 15:21 
------------------------
"""
import pytest,os
if __name__ == '__main__':
    pytest.main()
    # 想要自动生成报告，还要安装allure指令行
    os.system("allure generate ../report/exam -o ./report/html --clean")
    os.system("allure serve ../report/exam")