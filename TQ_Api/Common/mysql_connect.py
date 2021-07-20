#!/usr/bin/env python  
# encoding: utf-8   
""" 
------------------------
@author: Joey
@file: mysql_connect.py 
@time: 2021/6/24 15:37 
------------------------
"""
import pymssql
from Api.base_api import Logger
from Conf.read_conf import ini

class Mysql:
    def __init__(self):
        """初始化mysql的conn，连接数据库"""
    # 通过配置文件获取数据库的host，port，username，password，charset，database
        self.host = ini.get("mymssql","host")
        self.user = ini.get("mymssql","user")
        self.password = ini.get("mymssql","password")
        self.database = ini.get("mymssql","database")
        self.charset = ini.get("mymssql","charset")

        try:
            self.conn = pymssql.connect(self.host,self.user,self.password,self.database)
            print(f'成功链接数据库%s' % self.database)
        except Exception as e:
            Logger.error(f'连接数据库失败，原因:{e}')

    def select(self,query):
# 使用cursor()方法获取操作游标
        Logger.info(f'查询语句：{query}')
        try:
            self.cur = self.conn.cursor()
            # 执行SQL语句
            self.cur.execute(query)

            # 获取所有记录列表
            select_data = self.cur.fetchall()
            Logger.info("数据查询成功")

            # 返回select数据
            return select_data
        except Exception as e:
            Logger.error(f"select语句错误，错误原因是：{e}")


sql = Mysql()
if __name__ == '__main__':
    pass
    """
    sql = Mymssql()
    s = sql.select("select top 10 * from dbo.T_Orders WHERE ChargeAccount='18888888888' order by OrderTime desc;")
    for i in s:
        print(i)"""
