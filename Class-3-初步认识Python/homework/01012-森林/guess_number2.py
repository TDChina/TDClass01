# -*- coding: UTF-8 -*-
from random import randint


# 用户输入猜测的数字，返回int值
def gn():
    while True:
        try:
            g_num = int(raw_input())
            return g_num
        except ValueError:
            print 'ERROR,Please enter Numbers only: '


# 比较数字，返回提示
def guess(x, y):
    if x > y:
        return 'your guess is too big, try again: '
    elif x < y:
        return 'your guess is too small, try again: '
    elif x == y:
        return 'good job!'


print 'Guess a number between 0 and 100: '
rt_num = randint(0, 100)
g_times = 1  # 计次数
g = gn()

for i in xrange(0, 7):
    print guess(g, rt_num)
    if g == rt_num:
        print 'Use ' + str(g_times) + ' times!'
        break
    elif g_times == 7:  # 猜测7次错误，提示正确数字
        print 'Nope.The right number is %s' % rt_num
        break
    g_times += 1
    g = gn()
