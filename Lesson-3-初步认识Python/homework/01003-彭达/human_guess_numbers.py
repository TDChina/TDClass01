# encoding: utf-8
# file: human_guess_numbers
# author: cgpengda


import random


def main():
    rand_num = random.randint(0, 99)
    count = 1
    while count:
        input_num_str = raw_input(u"请输入一个0到99之间的整数：")
        if input_num_str.isdigit():
            input_num = int(input_num_str)
            if input_num > rand_num:
                print u"大了，再猜猜！"
            elif input_num < rand_num:
                print u"小了，再猜猜！"
            else:
                print u"答对了！"
                break
            count += 1
        else:
            print u"请输入一个整数!"


if __name__ == '__main__':
    main()
