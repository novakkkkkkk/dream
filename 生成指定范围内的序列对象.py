# !/usr/bin/env python 
# _*_ coding:utf-8 _*_
# 开发人员：liuzhe
# 开发时间：2019/11/7 11:34
# 文件名称：生成指定范围内的序列对象.PY
# 开发工具：PyCharm

def createList(listCount):
    list1=[]
    i=0
    while i<listCount:
        list1.append(i)
        i+=1
    return str(list1)

while 1:
    lastnum=input('请输入从0开始到生成该序列的总长度值：')
    print('已生成从0到',int(lastnum)-1,'的序列对象，该序列对象的字符串表达式为：',createList(int(lastnum)))