import random

times = 6		                                                                                #可以尝试的次数
number_min = 1                                                                                  #随机数生成范围最小值
number_max = 100                                                                                #随机数生成范围最大值

print '欢迎体验猜数字小游戏！^_^\n'
print '提示：默认随机数生成范围是1-100，可以尝试的机会为6次\n（输入“Y”即可进入修改界面，按回车直接开始游戏）\n是否需要修改：',
user = raw_input()
if user == "Y" or user == "y":
    number_min = int(raw_input("\n随机数最小值是："))
    number_max = int(raw_input("随机数最大值是："))
    times = int(raw_input("可以尝试的次数是："))
    
secret = random.randint(number_min,number_max)		                                            #生成随机数
number = raw_input("\n猜一下我心里在想哪个数字:")                                               #用户输入第一次的数字

while times > 0:
    times = times - 1
    if number.isdigit():
        guess = int(number)
        if guess == secret:
            print "\n哈哈！~~猜中了也没有奖励！"
            break
        else:
            if guess > secret:
                print "\n大了！大了！~~"
            else:
                print "\n小了！小了！~~"
            if times > 0:
                print "还有", times, "次机会哦!"
                number = raw_input("再试一次吧：")                                               #用户输入修改的数字
            else:
                print "\n机会用光咯,正确答案是：", secret
    else:
        times += 1
        number = raw_input("\n抱歉，您的输入有误，请输入一个整数：")                             #用户修改输入的格式
         
print "游戏结束，不玩啦~~"
