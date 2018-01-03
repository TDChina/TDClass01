# -*- coding: utf-8 -*-
import random


number = random.randint(0, 100)
# print "测试随值=>", number
count, more = 0, 5
while count <= more:
    # 次数小于或等于就循环
    while True:
        # 循环用户 输入非数字
        user_number = raw_input("请输入0-100间的整数：")
        if user_number.isdigit():
            user_number = int(user_number)
            break
        else:
            print "错误:请输入一个'整数'"
            
    if user_number > number:
        print "对不起，大了。你还有[", more - count, "]次机会。"
    elif user_number < number:
        print "对不起, 小了。你还有[", more - count, "]次机会。"
    else:
        print "恭喜你答对了。"
        break

    while count == more:
        # 循环 继续 与 退出 非指定字符
        user_continue_out = raw_input("'y'继续，'n'退出：")
        if user_continue_out == "y" or user_continue_out == "n":
            if user_continue_out == "y":
                count = 0
            elif user_continue_out == "n":
                break
        else:
            print "错误:只能输入一个小写字母'y'或'n'"

    count += 1
