# !/usr/bin/env python 
# _*_ coding:utf-8 _*_
# 开发人员：liuzhe
# 开发时间：2019/11/5 15:42
# 文件名称：倒计时.PY
# 开发工具：PyCharm
import datetime
day20=datetime.datetime.strptime('2020-1-25 0:0:0','%Y-%m-%d %H:%M:%S')
now=datetime.datetime.today()
delta=day20-now
day=delta.days
hour=int(delta.seconds/60/60)
minute=int((delta.seconds-hour*60*60)/60)
second=int(delta.seconds-hour*60*60-minute*60)
print('距离2020年春节还有：'+str(day)+'天'+str(hour)+'小时'+str(second)+'秒')