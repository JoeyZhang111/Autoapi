#!/usr/bin/env python  
# encoding: utf-8   
""" 
------------------------
@author: Joey
@file: fixture.py 
@time: 2021/7/19 14:18 
------------------------
"""
from api.login import Login
from api.base_api import BaseApi
import pytest

@pytest.fixture(scope="class",autouse=True)
def get_token():
    get = Login()
    get.send()
    BaseApi.token = get.get_res("$.token")