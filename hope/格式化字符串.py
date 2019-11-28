# !/usr/bin/env python 
# _*_ coding:utf-8 _*_
# 开发人员：liuzhe
# 开发时间：2019/11/25 10:06
# 文件名称：格式化字符串.PY
# 开发工具：PyCharm

template = '编号：{:0>9s}\t公司名称：{: <9s}\t官网： http://www.{:s}.com'  #定义模板
context1 = template.format('7','百度','baidu')
context2 = template.format('8','明日学院','mingrisoft')
context3 = template.format('9','金康高科','kingcome')
print(context1)
print(context2)
print(context3)