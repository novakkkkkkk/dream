# !/usr/bin/env python 
# _*_ coding:utf-8 _*_
# 开发人员：liuzhe
# 开发时间：2019/11/25 10:51
# 文件名称：根据身份证号判断生日性别.PY
# 开发工具：PyCharm

str1 = input('请输入您的身份证号：')
newstr1 = str1[6:10]+'年'+str1[10:12]+'月'+str1[12:14]+'日'
sexstr = int(str1[16])%2
sexstr = str(sexstr)
sexstr = sexstr.replace('1','男')
sexstr = sexstr.replace('0','女')
newstr1 = newstr1 + sexstr
print('您的生日和性别是：',newstr1)