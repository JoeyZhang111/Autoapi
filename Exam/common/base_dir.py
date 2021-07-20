#!/usr/bin/env python  
# encoding: utf-8   
""" 
------------------------
@author: Joey
@file: base_dir.py 
@time: 2021/7/5 16:32 
------------------------
"""
import os
BaseDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
api_path = os.path.join(BaseDir,"api")
common_path = os.path.join(BaseDir,"common")
conf_path = os.path.join(BaseDir,"conf")
data_path = os.path.join(BaseDir,"data")
log_path = os.path.join(BaseDir,"log")
report_path = os.path.join(BaseDir,"report")
testcase_path = os.path.join(BaseDir,"testcase")