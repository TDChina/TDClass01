# -*- coding: utf-8 -*-
import random

number = random.randint(0, 101)
count = 0
print "你有10次机会"
while count < 10:
    user_number = int(raw_input("请输入一个0-100之间的整数："))

    if user_number > number:
        print "(!-_-) 对不起 大了\n========================================"
    elif user_number < number:
        print "(-_-!) 对不起 小了\n========================================"
    elif user_number == number:
        print "(^0^) 恭喜你 答对了\n========================================"

    count += 1

    if count == 10 or user_number == number:
        user_10 = input("输入 ‘1’ 继续，输入‘0’ 退出：")
        if user_10 == 1:
            count = 0
        elif user_10 == 0:
            print "游戏结束"
            break
