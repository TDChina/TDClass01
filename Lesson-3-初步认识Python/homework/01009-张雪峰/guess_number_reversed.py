# *_*coding:utf-8 *_*
frequency = 1
while frequency == 1:
    in_num = raw_input('请输入一个100以内的整数：')
    if in_num.isdigit() == True and (0 < int(in_num) < 100):
        in_num = int(in_num)
        frequency_1 = 1
        num_max = 99
        num_min = 0
        num_mid = 50
        Times = 0
        while frequency_1 == 1:
            if num_mid == in_num:
                print("%s, 通过 %s 次计算得出" %(num_mid, Times))
                frequency_1 = 0
                frequency = 0
            elif num_mid > in_num:
                Times += 1
                num_max = num_mid
                num_mid = (num_max + num_min) / 2
            else:
                Times += 1
                num_min = num_mid
                num_mid = (num_max + num_min) / 2
    else:
        print "非法输入!!!!",
