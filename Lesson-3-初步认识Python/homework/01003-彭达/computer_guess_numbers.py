# encoding: utf-8
# file: computer_guess_numbers
# author: cgpengda


def main():
    print ""
    print ""
    print "-----------------------------------------------------------"
    print "-                                                         -"
    print "-   游戏规则：                                            -"
    print "-   先输入一个数字a,电脑猜一个数字b,给a,b判断大小：       -"
    print "-       当b > a时,输入反馈h（high）                       -"
    print "-       当b < a时,输入反馈l（low）                        -"
    print "-       当b = a时,输入反馈c（correct）                    -"
    print "-                                                         -"
    print "-----------------------------------------------------------"
    print ""
    print ""

    raw_input(u"请输入一个0到99之间的整数：")
    ranges = range(0, 100)
    front = 0
    end = len(ranges) - 1
    mid = (front + end) / 2

    count = 1
    while count:
        rand_num = ranges[mid]
        tags = raw_input(u"这个数字是：%s！" % str(rand_num))
        count += 1

        if tags.lower() == "h":
            end = mid - 1
            mid = (front + end) / 2
        elif tags.lower() == "l":
            front = mid + 1
            mid = (front + end) / 2
        elif tags.lower() == "c":
            print u"答对了！就是%s" % str(rand_num)
            break


if __name__ == "__main__":
    main()
