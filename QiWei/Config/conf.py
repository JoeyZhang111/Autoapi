#!/usr/bin/env python  
# encoding: utf-8   
""" 
------------------------
@author: Joey
@file: conf.py 
@time: 2021/6/9 11:48 
------------------------
"""
import configparser
from Common.handle_path import config_path
import os
#读取ini方法
class ReadIni():


    def __init__(self, file_path):
        self.conf = configparser.ConfigParser()
        self.conf.read(file_path)
    def get(self,options,values):
        value = self.conf.get(options,values)
        return value

# 调用对象
excelpath = os.path.join(config_path,"conf.ini")
conf = ReadIni(excelpath)


if __name__ == '__main__':
    """
    excelpath = os.path.join(config_path,"conf.ini")
    ini = ReadIni(excelpath)
    i = ini.get("excel","path")
    print(i)
"""
    # pass


