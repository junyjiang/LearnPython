#coding = utf-8
# -*- coding:utf-8 -*-
import re
x,y,z = re.split(':',input ('请输入三个数字，数字之间用空格隔开：'))
if(x>y):
    max1 = x
else:
    max1 = y
    if(z>max1):
        max1 = z
print max1