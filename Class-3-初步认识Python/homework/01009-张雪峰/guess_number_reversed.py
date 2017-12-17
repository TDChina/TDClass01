# *_*coding:utf-8 *_*
b=1
while b==1:
    in_num = raw_input('请输入一个100以内的整数：')
    if in_num.isdigit() == True  and int(in_num) < 100 and int(in_num) > 0:
        in_num=int(in_num)
        c=1
        num_max = 99
        num_min = 99
        num_var = 0
        while c == 1:
            if num_min == in_num:
                print(num_min)
                b = 0
                c = 0
            elif num_var == in_num:
                print(num_var)
                b = 0
                c = 0
            elif num_min > in_num or num_var > in_num:
                if num_var == 0:
                    num_max = num_min
                    num_min = num_max // 2
                else:
                    num_max = num_var
                    num_var = (num_max - num_min) // 2 + num_min
            else:
                if num_var == 0:
                    num_var = (num_max - num_min) // 2 + num_min
                else:
                    num_min = num_var
                    num_var = (num_max - num_min) // 2 + num_min
    else:
        print "非法输入!!!!",
