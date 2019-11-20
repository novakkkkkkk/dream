# !/usr/bin/env python 
# _*_ coding:utf-8 _*_
# 开发人员：liuzhe
# 开发时间：2019/11/7 15:23
# 文件名称：判断用户输入的字符是否为数字.PY
# 开发工具：PyCharm
def Validate_Is_Number(val):
    getASCII = ord(val)
    if getASCII >=48 and getASCII<=57:
        return True
    else:
        return False

while True:
    getnum = input("请输入一个有效数字")
    Is_Number = Validate_Is_Number(getnum)
    if Is_Number:
        print('您输入的是数字',getnum)
    else:
        print('您输入了非法字符，这里只能输入数字')
