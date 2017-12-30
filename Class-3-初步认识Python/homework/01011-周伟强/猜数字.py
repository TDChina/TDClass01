import random
a=random.randint(1,100)
x=0
while x < 10:
    n = raw_input('请输入一个数字：')
    if n.isdigit():
        n=int(n)
        if a == n:
            print '恭喜你，猜对了！！！这个数字为：',a
            break # 猜对的时候直接跳出本次循环
        elif a > n:
            print '猜小了！'
        else:
            print '猜大了！'
    else:
        print '只能输入整数数字，请重新输入！！'
        continue # 把输入有误的情况不记录在循环次数内。
    x+=1
else:
    print '你没有机会再猜了'

