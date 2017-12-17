# *_*coding:utf-8 *_*
import random
num=random.randint(0,100)
b = 1
while b == 1:
    in_num = raw_input('猜一猜数字(请输入一个100以内的整数)：')
    if in_num.isdigit() == True  and int(in_num) < 100 and int(in_num) > 0:
        in_num = int(in_num)
        if in_num == num:
            print "答对了",
            b=0
        elif in_num < num:
            print "小了小了",
        else:
            print "大了大了",
    else:
        print "非法输入!!!!",
