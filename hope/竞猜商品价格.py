# !/usr/bin/env python 
# _*_ coding:utf-8 _*_
# 开发人员：liuzhe
# 开发时间：2019/11/28 16:55
# 文件名称：竞猜商品价格.PY
# 开发工具：PyCharm
import random
goods = [['闪迪128G优盘','149'],['罗技鼠标','550'],['米家扫地机器人','1300'],['现代键盘','58']]
goodsel = list(random.choice(goods))

goodprice = int(goodsel[1])
print(goodsel[0])
for i in range(3):
    instr = int(input('请输入竞猜商品价格：'))
    if instr > goodprice:
        print('价格高了')
    elif instr < goodprice:
        print('价格太低了')
    else:
        print('恭喜您猜对了！')
        break