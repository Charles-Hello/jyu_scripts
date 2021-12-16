# -*- coding: utf-8 -*-
"""
@Time ： 2021/12/11 20:20
@Auth ： maomao
@File ：jyulogin.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""


import requests, sys, json,re
import urllib3
from requests.models import Response
urllib3.disable_warnings()

###填写参数####

# Corpid是企业号的标识
Corpid = "ww2fb0a8a29a34ef88"

# Secret是管理组凭证密钥
Secret = "BtreDqORADWa8q5N4w7K2rlxwDqqQ8JSamHOhUAFyPQ"

# 应用ID
Agentid = "1000003"

# token_config文件放置路径
Token_config = r'/ql/config/zabbix_wechat_config.json'

import hashlib
#输入密码


zhanghao = '181120127'
mima = 'aa15015'

sb = bytes(mima, encoding = "utf8")


upassfirst = hashlib.md5(b'2%s12345678'%sb).hexdigest()


upass =upassfirst +'123456782'





url = 'http://210.38.163.113/a30.htm'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.66'}
data = {
    'DDDDD': zhanghao,
    'upass': upass,
    'R1':0,
    'R2':1,
    'para':00,
    '0MKKey':'123456'}

res: Response = requests.post(url=url, data=data)
print(res.text)
m = '{}'.format(res.text)
m = re.findall(r'您已经成功登录',m)
print(m)









##下面的代码都不需要动###


def GetTokenFromServer(Corpid, Secret):
    """获取access_token"""
    Url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    Data = {
        "corpid": Corpid,
        "corpsecret": Secret
    }
    r = requests.get(url=Url, params=Data, verify=False)
    print(r.json())
    if r.json()['errcode'] != 0:
        return False
    else:
        Token = r.json()['access_token']
        file = open(Token_config, 'w')
        file.write(r.text)
        file.close()
        return Token


def SendMessage(Partyid, Subject, Content):
    """发送消息"""
    # 获取token信息
    try:
        file = open(Token_config, 'r')
        Token = json.load(file)['access_token']
        file.close()
    except:
        Token = GetTokenFromServer(Corpid, Secret)

    # 发送消息
    Url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s" % Token
    Data = {
        "touser": touser,
        "msgtype": "text",
        "agentid": Agentid,
        "text": {"content": Subject + '\n' + Content},
        "safe": "0"
    }
    r = requests.post(url=Url, data=json.dumps(Data), verify=False)

    # 如果发送失败，将重试三次
    n = 1
    while r.json()['errcode'] != 0 and n < 4:
        n = n + 1
        Token = GetTokenFromServer(Corpid, Secret)
        if Token:
            Url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s" % Token
            r = requests.post(url=Url, data=json.dumps(Data), verify=False)
            print(r.json())

    return r.json()


if __name__ == '__main__':
    # 部门id
    touser = '@all'
    # 消息标题
    Subject = '嘉应校园网'
    # 消息内容
    Content = str(m)
    Status = SendMessage(touser, Subject, Content)
    print(Status)