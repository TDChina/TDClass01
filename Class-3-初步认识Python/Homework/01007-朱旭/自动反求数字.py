import random

number_min = 0                                      #随机数生成范围最小值
number_max = 100                                    #随机数生成范围最大值

print("欢迎体验反求数字小游戏！^_^\n")
key = 1
while key == 1:
    print("\n提示：默认随机数生成范围是0-100\n（输入“Y”即可进入修改界面，按回车直接开始游戏）\n是否需要修改:", end="")
    user = input()
    if user == "Y" or user == "y":
        print("\n随机数最小值是:", end="")
        number_min_input = input()
        number_min = int(number_min_input)
        print("随机数最大值是:", end="")
        number_max_input = input()
        number_max = int(number_max_input )
        
    secret = random.randint(number_min,number_max)		#随机数
    number = int((number_min + number_max) * 0.5)       #反求数
    multiple = 2                                        #倍数
    times = 0                                           #次数
    
    while True:
        if number == secret:
            print("\n正确答案是:", secret, ",我只猜了", times, "次哦^_^！")
            key = 0
            break
                
        elif number < secret:
            print("\n小了！小了！~~")
            multiple *= 2
            times += 1
            range = int(number_max/multiple) + 1
            print(number, "+", range, "=", (number + range))
            number = int(number + range)
            
        elif number > secret:
            print("\n大了！大了！~~")
            multiple *= 2
            times += 1
            range = int(number_max/multiple) + 1
            print(number, "-", range, "=", (number - range))
            number = int(number - range)
        
    print("还要再来猜一次吗？(输入”Y“再玩一次，按回车退出开始游戏)")
    user = input()
    if user == "Y" or user == "y":
        key = 1

print("\n下次再来玩哦^_^!~~")
