#!/usr/bin/env python  
# encoding: utf-8   
""" 
------------------------
@author: Joey
@file: handle_path.py 
@time: 2021/6/1 14:41 
------------------------
"""
import os
BaseDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
api_path = os.path.join(BaseDir,"api")
common_path = os.path.join(BaseDir,"Common")
config_path = os.path.join(BaseDir,"Config")
report_path =os.path.join(BaseDir,"Report")
log_path = os.path.join(BaseDir,"Log")
data_path = os.path.join(BaseDir,"Data")
testcase_path = os.path.join(BaseDir,"TsatCase")

"""
print(api_path)
print(common_path)
print(config_path)
print(report_path)
print(data_path)
print(testcase_path)
"""