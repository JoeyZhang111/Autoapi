#!/usr/bin/env python  
# encoding: utf-8   
""" 
------------------------
@author: Joey
@file: get_conf.py 
@time: 2021/7/16 14:42 
------------------------
"""
import configparser,os
from common.base_dir import conf_path
#读取ini方法
class ReadIni():
    def __init__(self,name):
       self.conf = configparser.ConfigParser()
       self.conf.read(name)
    def get(self,options,values):
        value = self.conf.get(options,values)
        return value

# 调用对象
path = os.path.join(conf_path,"conf.ini")
ini = ReadIni(path)