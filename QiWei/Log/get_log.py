#!/usr/bin/env python  
# encoding: utf-8   
""" 
------------------------
@author: Joey
@file: get_log.py 
@time: 2021/6/7 16:50 
------------------------
"""
from loguru import logger
import os
import time



class Logger:
    '''
    日志类
    '''

    def __init__(self,name):
        logger.add(name)

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


if __name__ == "__main__":
    """
    timer = time.localtime(time.time())
    log_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'excute', f'runtime_{timer}.log')
    logger.add(log_name,rotation='100 MB', retention='7 days', enqueue=True, encoding='utf-8')
    logger.info("----- 开始----")
    logger.info("----- Execute Ending-----")
"""
    pass