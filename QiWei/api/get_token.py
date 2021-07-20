#!/usr/bin/env python  
# encoding: utf-8   
""" 
------------------------
@author: Joey
@file: get_token.py 
@time: 2021/5/28 13:45 
------------------------
"""

from api.base_api import BaseApi
class GetToken(BaseApi):
    def __init__(self):
        #先实现父类的初始化函数
        BaseApi.__init__(self)
        self.url = self.host + "/cgi-bin/gettoken"
        self.method = "get"
        self.params = {
            "corpid":"wwc51cca3120b64bba",
            "corpsecret":"zXcmKYQrfXjmaHpcBcbs33k1_O6lVz8-Fk39FM4Ro3Q"
        }
get_token =GetToken()
print(get_token)
a=get_token.send()
print(a)
token = get_token.get_res('$.access_token')
if __name__ == '__main__':
    pass
# get_token =GetToken()
# get_token.send()
#token = get_token.get_res('$.access_token')
# # print(token)






"""
url="https://qyapi.weixin.qq.com/cgi-bin/gettoken"
params = {"corpid":"wwc51cca3120b64bba",
          "corpsecret":"zXcmKYQrfXjmaHpcBcbs33k1_O6lVz8-Fk39FM4Ro3Q"}
r = requests.get(url,params)
print(jsonpath.jsonpath(r.json(),'$.access_token')[0])
"""