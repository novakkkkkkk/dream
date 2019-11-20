# !/usr/bin/env python 
# _*_ coding:utf-8 _*_
# 开发人员：liuzhe
# 开发时间：2019/11/6 10:24
# 文件名称：根据输入的年份 计算年龄大小.PY
# 开发工具：PyCharm
import datetime
imyear = input('请输入您的出生年份：')
nowyear = datetime.datetime.now().year
age = nowyear-int(imyear)
print('您的年龄为：',age,'岁')
if age<18:
    print('您现在为未成年人')
if age>=18 and age<66:
    print('您现在为青年人')
if age>=66 and age<80:
    print('您现在为中年人')
if age>=80:
    print('您现在为老年人')