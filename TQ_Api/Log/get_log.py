#!/usr/bin/env python  
# encoding: utf-8   
""" 
------------------------
@author: Joey
@file: get_log.py 
@time: 2021/6/30 16:28 
------------------------
"""
from loguru import logger
import os
from Common.base_dir import log_path
class Logger:
    def __init__(self):
        name = os.path.join(log_path,'execute','time_{time}.log')
        # print(name)
        logger.add(name,rotation='100 MB', retention='3 days', enqueue=True, encoding='utf-8')
    def info(self, msg):
        '''打印 info 级别的日志'''
        logger.info(msg)

    def debug(self, msg):
        '''打印 debug 级别的日志'''
        logger.debug(msg)

    def warning(self, msg):
        '''打印 warning 级别的日志'''
        logger.warning(msg)

    def error(self, msg):
        '''打印 error 级别的日志'''
        logger.error(msg)

Logger()

if __name__ == '__main__':
    pass