# !/usr/bin/env python 
# _*_ coding:utf-8 _*_
# 开发人员：liuzhe
# 开发时间：2019/11/20 14:31
# 文件名称：查找字符串中的字符.PY
# 开发工具：PyCharm

word = 'ArrayListCharacter listnewArrayList3125'
while 1:
       instr = input('请输入要查找的字符或字符串：')
       print(word + '包含' + instr + ' 共计：' + str(word.count(instr)))
