#!/usr/bin/env python  
# encoding: utf-8   
""" 
------------------------
@author: Joey
@file: base_dir.py 
@time: 2021/6/18 11:39 
------------------------
"""

import os
BaseDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
api_path = os.path.join(BaseDir,"Api")
common_path = os.path.join(BaseDir,"Common")
conf_path = os.path.join(BaseDir,"Conf")
data_path = os.path.join(BaseDir,"Data")
log_path = os.path.join(BaseDir,"Log")
rep_path = os.path.join(BaseDir,"Report")
testcase_path = os.path.join(BaseDir,"TestCase")

# print(log_path)

