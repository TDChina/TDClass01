import random

times = 6		                                    #可以尝试的次数
number_min = 1                                      #随机数生成范围最小值
number_max = 100                                    #随机数生成范围最大值

print("欢迎体验猜数字小游戏！^_^\n")
print("提示：默认随机数生成范围是1-100，可以尝试的机会为6次\n（输入“Y”即可进入修改界面，按回车直接开始游戏）\n是否需要修改：", end="")
user = input()
if user == "Y" or user == "y":
    print("\n随机数最小值是：", end="")
    number_min_input = input()
    number_min = int(number_min_input)
    print("随机数最大值是：", end="")
    number_max_input = input()
    number_max = int(number_max_input )
    print("可以尝试的次数为：", end="")
    times_input = input()
    times = int(times_input)
    
secret = random.randint(number_min,number_max)		# 生成随机数

print("\n猜一下我心里在想哪个数字","（", number_min, "-", number_max, "）:", end="")
while times > 0:
    number = input()
    times = times - 1
    
    if number.isdigit():
        guess = int(number)
        
        if guess == secret:
            print ("哈哈！~~猜中了也没有奖励！")
            break
        
        else:
            if guess > secret:
                print ("大了！大了！~~")
            else:
                print ("小了！小了！~~")
            if times > 0:
                print("还有",times,"次机会哦!再试一次吧：",end="")
            else:
                print("机会用光咯,正确答案是：",secret)
				
    else:
         times += 1
         print("抱歉，您的输入有误，请输入一个整数：",end="")
		
print ("游戏结束，不玩啦~~")
