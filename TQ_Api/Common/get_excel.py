#!/usr/bin/env python  
# encoding: utf-8   
""" 
------------------------
@author: Joey
@file: excel.py 
@time: 2021/5/19 17:46 
------------------------
"""
import xlrd,os,json
from Common.base_dir import data_path
from Conf.read_conf import ini
class GetData:
    def __init__(self,path,sheetname):
        self.workbook = xlrd.open_workbook(path)
        self.sheet = self.workbook.sheet_by_name(sheetname)

    def get_data(self):
        list = []
# print(sheet.nrows)#打印最大行数
        for i in range(1, self.sheet.nrows):
            id = self.sheet.cell(i,0).value
            name = self.sheet.cell(i,2).value
            url = self.sheet.cell(i,3).value
            method = self.sheet.cell(i,4).value
            reqbody = self.sheet.cell(i,5).value
            respdata = self.sheet.cell(i,7).value#期望数据
            # 字符串格式--不能使用键去取,strict=False参数，来兼容非标准格式
            # body = json.loads(body,strict=False)
            # respdata = json.loads(respdata)["Code"]
            # r = eval(respdata)
            list.append((id,name,url,method,reqbody,respdata))
        return list
    def close(self):
        self.workbook.close()

# 其他文件引用调用以下对象
"""
data_path = os.path.join(data_path,ini.get("excel","path"))
sheetname = ini.get("excel","sheetname1")
data = GetData(data_path,sheetname)
get_data = data.get_data()"""

