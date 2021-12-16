# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/11/29 14:25
# @Author : Mr.Miao
# @Email : 1140601003@qq.com
# @Wechat : a1140601003
# @Software: PyCharm


import re
import requests

'''
只需要配置俩个参数YOUR_buildingID和YOUR_roomID即可获取自己宿舍电费余额
'''
'''YOUR_buildingID的值为⬇️面的找出来自己住的宿舍'''
'''YOUR_roomID的值为自己住的宿舍号码'''

YOUR_buildingID ='10136'
YOUR_roomID ='413'


'''
"南1栋",
"8158"

"南2栋",
"8271"


"南3栋",
"8384"


"南4栋",
"8476"


"南5栋",
"8554"


"南6栋",
"8675"


"南7栋",
"8780"


"南8栋",
"8981"


"中1E栋",
"9102"


"中2左栋",
"9150"


"中2右栋",
"9216"


"中3栋",
"9242"


"中4A栋",
"9318"


"中4B栋",
"9367"


"中5栋",
"9416"


"中6栋",
"9507"


"东3栋",
"9553"


"东5栋",
"9574"


"东6栋",
"9605"


"东8栋",
"9627"


"东9栋",
"9648"


"东12栋",
"9719"


"东13栋",
"9780"


"东14栋",
"9841"


"东15栋",
"9902"


"东16栋",
"9973"


"东17栋",
"10136"


"东18A栋",
"10305"


"东18B栋",
"10396"


"东18C栋",
"10475"


"东18D栋",
"10554"


"东18E栋",
"10633"


"东19栋",
"10724"


"中1A栋",
"10907"


"中1B栋",
"10999"


"中1C栋",
"11091"


"中1D栋",
"11154"
'''



url = 'http://210.38.163.34:8090/sdms-select/webSelect/roomFillLogView.do'
headers = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.9',
'Connection': 'keep-alive',
'Host': '210.38.163.34:8090',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36',
}

get_headers = requests.get(url=url, headers=headers).headers

# print(get_headers['Set-Cookie'])

result = get_headers['Set-Cookie']

get_first = re.search(r'JSESSIONID=.*?;',result)

# print(get_first[0])

final = get_first[0].replace(';','')

# print(type(final))


min_url = 'http://210.38.163.34:8090/sdms-select/webSelect/roomFillLogView.do'

min_header ={
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Cache-Control': 'max-age=0',
'Connection':'keep-alive',
'Content-Length':'29',
'Cookie': final,
'Origin': 'http://210.38.163.34:8090',
'Host': '210.38.163.34:8090',
'Referer': 'http://210.38.163.34:8090/sdms-select/webSelect/roomFillLogView.do',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.34',
}

playdata = {
'buildingId': YOUR_buildingID,
'roomName': YOUR_roomID
}

min_room = requests.post(url=min_url,headers=min_header,data=playdata)


last_url = 'http://210.38.163.34:8090/sdms-select/webSelect/welcome2.jsp'

last_header ={
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
'Connection':'keep-alive',
'Cache-Control': 'no-cache',
'Cookie': final,
'Host': '210.38.163.34:8090',
'Referer': 'http://210.38.163.34:8090/sdms-select/webSelect/roomFillLogView.do',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.34',
}

get_jsp = requests.get(url=last_url,headers=last_header)

final_html = get_jsp.text


from lxml import etree

html = etree.HTML(final_html)

divs = html.xpath('//tr[@class]')
# print(divs)
d = etree.tostring(divs[-6],encoding= 'utf8').decode('utf8')
# print(d)

messagespro = d.split("\n")
# print(messagespro[1])
# print(messagespro[4])


haoma = re.findall(r' .*?<',messagespro[1])
dianfei = re.findall(r' .*?<',messagespro[4])
print(haoma[1].replace('<',''))
print('电费剩余'+dianfei[1].replace('<','')+'度')

