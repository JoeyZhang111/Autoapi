#!/usr/bin/env python  
# encoding: utf-8   
""" 
------------------------
@author: Joey
@file: read_conf.py 
@time: 2021/6/18 11:47 
------------------------
"""
import configparser
from Common.base_dir import conf_path
import os
#读取ini方法
class ReadIni():
    def __init__(self,filename):
        self.conf = configparser.ConfigParser()
        self.conf.read(filename)
    def get(self,options,values):
        value = self.conf.get(options,values)
        return value
# 调用对象
path = os.path.join(conf_path,"conf.ini")
ini = ReadIni(path)
# i = ini.get("url","host1")
# print(i)