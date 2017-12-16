# -*- coding: UTF-8 -*-


# 取中值
def median(min_num, max_num):
    med_num = min_num + (max_num - min_num) / 2
    if max_num - min_num == 1:
        med_num = max_num
    return med_num


# 初始化
g_times = 1  # 计次
mn_num = 0
mx_num = 100
my_guess = 0

# 说明
print '***  You can enter a number between %d and %d    ***' % (mn_num, mx_num)
print '***  Then I will try to guess the right number   ***'
print '***  [B/S] means Big or Small                    ***\n'

# 输入判定
print 'Please enter a number between %s and %s: ' % (mn_num, mx_num),
while True:
    try:
        rt_num = int(raw_input())
    except ValueError:
        print 'ERROR,Please enter Numbers only: ',
        continue
    if mn_num <= rt_num <= mx_num:
        break
    else:
        print 'ERROR!Number must between %s and %s: ' % (mn_num, mx_num),
        continue

# 电脑猜测
print '\n''okay, I guess the number is %d!' % my_guess
if my_guess == rt_num:  # 如果0为正确数
    print "Unbelievable!!I guessed it at the first time!"
else:
    while True:
        bs = raw_input('Wrong...too big or too small? [B/S]: ')
        if bs.lower() in ['b', 'big']:
            if my_guess <= mn_num:  # 逻辑判断
                print 'Smaller than %d!? You cheated me!!' % mn_num
                break
            elif my_guess == mx_num:  # 逻辑判断
                print 'Emm???????!! You cheated me!!'
                break
            mx_num = my_guess
            my_guess = median(mn_num, mx_num)  # 取中位数
        elif bs.lower() in ['s', 'small']:
            if my_guess >= mx_num:  # 逻辑判断
                print 'Bigger than %d!? You cheated me!!' % mx_num
                break
            elif my_guess == mn_num and my_guess != 0:  # 逻辑判断
                print 'Emm???????!! You cheated me!!'
                break
            mn_num = my_guess
            my_guess = median(mn_num, mx_num)  # 取中位数
        else:
            bs = raw_input(
                'ERROR! Please enter letter B or S (case-insensitive): ')
            continue

        print '\n''Emm...I guess the number is %d!' % my_guess
        g_times += 1
        if my_guess == rt_num:
            print 'Aha! I guessed it with %s times.' % g_times
            break
        elif mn_num == mx_num:  # 逻辑判断
            print 'Emm???????!! You cheated me!!'
            break
