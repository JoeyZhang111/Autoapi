#!/usr/bin/env python  
# encoding: utf-8   
""" 
------------------------
@author: Joey
@file: get_data.py 
@time: 2021/5/31 16:12 
------------------------
"""
from Common.handle_path import data_path
import xlrd,os,json
class GetData:
    def __init__(self,path,sheetname):
        self.wb = xlrd.open_workbook(path)
        self.sheet = self.wb.sheet_by_name(sheetname)
    def get_data(self):
        list =[]
        for i in range(1,self.sheet.nrows):
            id = self.sheet.cell(i,0).value
            name = self.sheet.cell(i,1).value
            url = self.sheet.cell(i,2).value
            method = self.sheet.cell(i,3).value
            reqbody = self.sheet.cell(i,4).value
            expect = self.sheet.cell(i,5).value
            # list.append((url, method,reqbody,expect))
            # 字符串格式--不能使用键去取
            # reqbody = json.loads(reqbody)
            # expect = json.loads(expect)
            list.append((id,name,url,method,reqbody,expect))
        return list
    def close(self):
        self.wb.close()


if __name__ == '__main__':
    """
    path = os.path.join(data_path, "qiwei.xlsx")
    data = GetData(path, "create")
    get = data.get_data()

    print(get)
    """
    pass


