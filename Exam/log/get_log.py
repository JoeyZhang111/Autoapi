#!/usr/bin/env python  
# encoding: utf-8   
""" 
------------------------
@author: Joey
@file: get_log.py 
@time: 2021/7/19 10:48 
------------------------
"""
from loguru import logger
import os
from common.base_dir import log_path
class Logger:
    def __init__(self):
        name = os.path.join(log_path,"runtime","time_{time}.log")
        logger.add(name,rotation='10 MB', retention='3 days', enqueue=True, encoding='utf-8')

    def info(self,msg):
        logger.info(msg)
    def debug(self,msg):
        logger.debug(msg)
    def error(self,msg):
        logger.error(msg)
    def critical(self,msg):
        logger.critical(msg)
    def warning(self,msg):
        logger.warning(msg)


Logger()
