# -*- coding: utf-8 -*-
import random, time

while True:
    # 循环非数字
    user_number = raw_input("请输入0-100之间的整数让我猜猜你输入的是什么：")
    if user_number.isdigit():
        user_number = int(user_number)
        break
    else:
        print "错误:请输入一个'整数'数字"

ai_min_number, ai_max_number = 0, 101
ai_range_number = range(ai_min_number, ai_max_number)
ai_rand_number = random.sample(ai_range_number, 1)

count = 1
while ai_rand_number != user_number:
    # 不等于用户输入 就循环 并计数
    ai_range_number = range(ai_min_number, ai_max_number)
    ai_rand_number = random.sample(ai_range_number, 1)

    if ai_rand_number[0] > user_number:
        print "我猜是==>", ai_rand_number[0], "\n好像大了让我再想想。。。"
        ai_max_number = ai_rand_number[0]
        ai_rand_number = random.sample(ai_range_number, 1)
        time.sleep(1)
    elif ai_rand_number[0] < user_number:
        print "我猜是==>", ai_rand_number[0], "\n好像小了让我再想想。。。"
        ai_min_number = ai_rand_number[0] + 1
        aiRand = random.sample(ai_range_number, 1)
        time.sleep(1)
    else:
        print "这次猜不对我就‘死机’!!!\n我猜是==>", ai_rand_number[0]
        time.sleep(1)
        break

    count += 1

print "恭喜我(^0^) 答对了, 我一共猜了【", count, "】次就答对了"
