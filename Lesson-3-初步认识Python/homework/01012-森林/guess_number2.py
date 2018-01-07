# -*- coding: UTF-8 -*-
from random import randint


def guess_input():
    """
        函数开始运行后，程序将阻断并等待用户输入猜测的数字。
        如果用户没有正确输入，此函数将阻断程序运行并要求用户重新输入数字。
        用户输入合法数字时，函数将返回词值。
    :return:
        当用户正确输入的情况下返回一个int型数值。
    """
    while True:
        try:
            g_num = int(raw_input())
            return g_num
        except ValueError:
            print 'ERROR,Please enter Numbers only: '


def guess(guess_num, right_num):
    """
        用来比较用户猜测的数字和正确的数字
    :param guess_num: 用户猜测的数字
    :param right_num: 正确的数字
    :return:
        返回提示信息
    """
    if guess_num > right_num:
        return 'your guess is too big, try again: '
    elif guess_num < right_num:
        return 'your guess is too small, try again: '
    else:
        return 'good job!'


# 初始化
g_times = 1  # 计次数
max_times = 7  # 最大猜测次数
mn_num = 0  # 猜测范围最小值
mx_num = 100  # 猜测范围最大值
rt_num = randint(mn_num, mx_num)

print 'Guess a number between %s and %s: ' % (mn_num, mx_num)
while True:
    g = guess_input()
    print guess(g, rt_num)
    if g == rt_num:
        print 'Use ' + str(g_times) + ' times!'
        break
    elif g_times == max_times:  # 猜测7次错误，提示正确数字
        print 'Nope.The right number is %s' % rt_num
        break
    g_times += 1

