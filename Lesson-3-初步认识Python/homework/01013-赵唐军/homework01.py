# _*_ coding: utf-8 _*_
# __author__ = "ZhaoTangjun"


import random

input_num = random.randint(1, 100)
times = 10

while times:
    times = times - 1
    guess_num = int(raw_input("����10�λ�������֣�����%s�Σ�������һ��1-100�����֣�" % times))
    if guess_num > input_num:
        print"�е���ˣ���"
    elif guess_num < input_num:
        print"�е�С�ˣ���"
    if guess_num == input_num:
        print"��ϲ�㣬�¶��ˣ���"
        break