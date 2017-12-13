print('欢迎使用十进制转换器!\n')
while True:
    parm = input('请输入一个整数（输入Q结束程序）\n：')
    check = parm.isdigit()
    
    if parm == 'Q' or parm == 'q':
        print('\n谢谢您的使用！\n')
        break
        
    elif check != True:
            print( '\n\n请输入一个整数类型！\n')
            continue
        
    num = int(parm)
    parm = str('parm')
 
    #print('\t十六进制：0x%x' % num)
    print('\t十六进制 ： {0}'.format('%#x' % num))
    print('\t八进制 ： {0}'.format('%#o' % num))
    print('\t二进制 ：', bin(num), '\n'* 6)

