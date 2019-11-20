# !/usr/bin/env python 
# _*_ coding:utf-8 _*_
# 开发人员：liuzhe
# 开发时间：2019/11/20 11:28
# 文件名称：字符串综合训练.PY
# 开发工具：PyCharm

bzs = '2018 Amazon Jeff Bezos 1120'
word = '美国企业请注意，要么创新，要么杰夫.贝佐斯替你创新'
# 第一题答案，去掉2018的两种方法
print(bzs[5:])
print(bzs.replace('2018','').strip())
# 第二题答案，得到数字20181120的方法
print(bzs[0:4]+bzs[23:])
# 第三题答案，
print('【'+bzs[0:4]+'】'+bzs[5:23]+'【'+bzs[23:27]+'】')