import random
randNum = random.randint(1, 100)
countNum = 0

print '!!!You just have 6 times to win this game.!!!'
print ''

while True:
    entNum = raw_input('Enter a number from 1-100:')
    if entNum.isdigit() and 0 < int(entNum) <101:
        countNum = countNum + 1
        chanceNum = 6 - countNum
        entNum = int(entNum)
        if entNum == randNum:
            print 'You win\n You usead', countNum, 'times'
            break
        elif entNum > randNum:
            print 'The number is big'
        elif entNum < randNum:
            print 'The number is small'
        if countNum >= 6:
            print 'You lose\n The number is', randNum
            break
        if chanceNum == 1:
            print '(This is the last 1 chance)'
        else:
            print '(You stil have {0} times)'.format(chanceNum)
    else:
        print 'Enter erro, Please try again.'
        continue
