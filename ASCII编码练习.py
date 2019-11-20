# !/usr/bin/env python 
# _*_ coding:utf-8 _*_
# 开发人员：liuzhe
# 开发时间：2019/11/6 9:16
# 文件名称：ASCII编码练习.PY
# 开发工具：PyCharm
print('a')
print(chr(97))
print('A')
print(chr(65))
print(chr(43))
print(chr(93))
print(chr(127))
print(chr(94))
print('\u4e2d\u56fd')
fp = open(r'D:\mr.txt','a+')
print('要么出局，要么出众', file=fp)
fp.close()