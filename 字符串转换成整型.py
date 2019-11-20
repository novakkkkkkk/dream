# !/usr/bin/env python 
# _*_ coding:utf-8 _*_
# 开发人员：liuzhe
# 开发时间：2019/11/7 10:23
# 文件名称：字符串转换成整型.PY
# 开发工具：PyCharm

while 1:
    getnum=input('请输入一个数字：')
    try:
        g=int(getnum)
        print('您输入的是数字：',g)
    except:
        print('==您输入的不是数字==')