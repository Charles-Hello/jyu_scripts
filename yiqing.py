# -*- coding: utf-8 -*-
"""
@Time ： 2021/12/16 00:35
@Auth ： maomao
@File ：yiqing.py.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
import requests

headers = {
    'Content-Type': 'application/json',
    'Atimestamp': '1639585915',
    'Host': 'api.jyu.edu.cn',
    'x-tif-sid': 'ec2c3294244640b4b08c3c19889f9412',
    'Asecret': '5c74a2f678ae92b496f7277da59b3f82',
    'Referer': 'https://servicewechat.com/wx84ddfd51a823dc58/141/page-frame.html',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.16(0x18001039) NetType/WIFI Language/zh_CN',
    'Connection': 'keep-alive',
}

params = (
    ('sid', 'ec2c3294244640b4b08c3c19889f9412'),
)

data = '{"studentid":"181120127"}'

response = requests.post('https://api.jyu.edu.cn/wxapi/Tongxingzheng/info', headers=headers, params=params, data=data, verify=False)
print(response.text)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.post('https://api.jyu.edu.cn/wxapi/Tongxingzheng/info?sid=ec2c3294244640b4b08c3c19889f9412', headers=headers, data=data, verify=False)