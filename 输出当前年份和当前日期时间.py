# !/usr/bin/env python 
# _*_ coding:utf-8 _*_
# 开发人员：liuzhe
# 开发时间：2019/11/6 9:26
# 文件名称：输出当前年份和当前日期时间.PY
# 开发工具：PyCharm
import datetime
print('当前年份：'+str(datetime.datetime.now().year))
print('当前月份：'+str(datetime.datetime.now().month))
print('当前日期：'+str(datetime.datetime.now().day))
print('')
print('当前日期时间：'+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))