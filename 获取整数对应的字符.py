# !/usr/bin/env python 
# _*_ coding:utf-8 _*_
# 开发人员：liuzhe
# 开发时间：2019/11/7 16:52
# 文件名称：获取整数对应的字符.PY
# 开发工具：PyCharm

result=[]
s='bcdefghijk'
for i in s:
    up = chr(ord(i)-1)
    result.append(up)
print(''.join(result))