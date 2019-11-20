# !/usr/bin/env python 
# _*_ coding:utf-8 _*_
# 开发人员：liuzhe
# 开发时间：2019/11/7 10:18
# 文件名称：十进制转换为二进制.PY
# 开发工具：PyCharm

def compare2(c):
    con2=bin(c)
    return con2[2:]
while 1:
    getnum=input('请输入一个数字：')
    print(compare2(int(getnum)))