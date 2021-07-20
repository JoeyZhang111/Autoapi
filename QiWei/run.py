#!/usr/bin/env python  
# encoding: utf-8   
""" 
------------------------
@author: Joey
@file: run.py 
@time: 2021/5/31 11:44 
------------------------
"""
import pytest,os
if __name__ == '__main__':
    pytest.main()
    # 想要自动生成报告，还要安装allure指令行
    os.system("allure generate ./Report/wx -o ./Report/html --clean")
    os.system("allure serve ./Report/wx")