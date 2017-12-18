# -*- coding: utf-8 -*-
import random
import time

userNum = int(raw_input("请输入0-100之间的整数让我猜猜你输入的是什么："))
aiMin, aiMax = 0, 101
list = range(aiMin, aiMax)
aiRand = random.sample(list, 1)
count = 1
while aiRand != userNum:
    list = range(aiMin, aiMax)
    aiRand = random.sample(list, 1)
    if aiRand[0] > userNum:
        print "我猜是==>", aiRand[0], "\n好像大了让我再想想。。。"
        aiMax = aiRand[0]
        aiRand = random.sample(list, 1)
        time.sleep(2)
    elif aiRand[0] < userNum:
        print "我猜是==>", aiRand[0], "\n好像小了让我再想想。。。"
        aiMin = aiRand[0] + 1
        aiRand = random.sample(list, 1)
        time.sleep(2)
    elif aiRand[0] == userNum:
        print "这次猜不对我就‘死机’!!!\n我猜是==>", aiRand[0]
        time.sleep(2)
        break
    count += 1
print "恭喜我(^0^) 答对了, 我一共了【", count, "】次就答对了"