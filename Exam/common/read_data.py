#!/usr/bin/env python  
# encoding: utf-8   
""" 
------------------------
@author: Joey
@file: read_data.py 
@time: 2021/7/19 10:20 
------------------------
"""
import xlrd,os
from common.base_dir import data_path
from conf.get_conf import ini
class GetData:
    def __init__(self,path,sheetname):
        self.wb = xlrd.open_workbook(path)
        self.sheet = self.wb.sheet_by_name(sheetname)
    def get_data(self):
        list = []
        for i in range(1,self.sheet.nrows):
            id = self.sheet.cell(i,0).value
            name = self.sheet.cell(i,1).value
            url = self.sheet.cell(i,3).value
            method = self.sheet.cell(i,4).value
            body = self.sheet.cell(i,5).value
            res = self.sheet.cell(i,7).value
            list.append((id,name,url,method,body,res))
        return  list
    def close(self):
        self.wb.close()

"""
path = os.path.join(data_path, ini.get("excel", "path"))
data = GetData(path, ini.get("excel", "sheetname1"))
test_data = data.get_data()
print(test_data)
"""



