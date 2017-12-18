# _*_ coding: utf-8 _*_


import random

input_num = random.randint(1, 100)
times = 10

while times:
    times = times - 1
    guess_num = int(raw_input("你有10次机会猜数字，还有%s次，请输入一个1-100的数字：" % times))
    if guess_num > input_num:
        print"有点大了！！"
    elif guess_num < input_num:
        print"有点小了！！"
    if guess_num == input_num:
        print"恭喜你，猜对了！！"
        break