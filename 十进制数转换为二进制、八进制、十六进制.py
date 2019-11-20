# !/usr/bin/env python 
# _*_ coding:utf-8 _*_
# 开发人员：liuzhe
# 开发时间：2019/11/8 10:45
# 文件名称：十进制数转换为二进制、八进制、十六进制.PY
# 开发工具：PyCharm
while 1:
     number =int(input('请输入一个十进制数：'))
     two = bin(number)[2:]
     eight = oct(number)[2:]
     sixteen = hex(number)[2:]
     print(number,'的二进制数为',two,',八进制数为',eight,',十六进制数为',sixteen)