# -*- coding: utf-8 -*-
"""
@Time ： 2021/12/15 23:21
@Auth ： maomao
@File ：jyu疫情.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
import re
import random
import base64

list_nv = ['黄若菡', '张盼灵', '陈语蓉', '黄巧晴', '黄芷梦', '黄晓萱', '黄紫汶']
list_nan = ['黄昭南', '黄玄羽', '黄泽禹', '黄绅绮', '黄沐锋', '黄志文', '黄翔宇']
nanNAME = list_nan[random.randint(0, 6)]
nanNV = list_nan[random.randint(0, 6)]
print(nanNAME)
print(nanNV)

jpg_random = random.randint(0, 4)
img_path_nan = 'nan{name}.jpg'.format(name=jpg_random)
img_path_nv = 'nv{name}.jpg'.format(name=jpg_random)

print(img_path_nan)
with open(img_path_nan, 'rb') as f:
    base64_data = base64.b64encode(f.read())
    tupian = base64_data.decode()
    print('data:image/jpeg;base64,%s'%tupian)
