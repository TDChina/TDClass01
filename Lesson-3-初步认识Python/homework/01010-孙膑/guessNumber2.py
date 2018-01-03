print '''You think a number and let me gess.
         Please give me some hints
         If I guess the number is biger, Enter 'big'
         If I guess the number is smaller, Enter 'small'
         If I guess the number is right,Enter 'yes'
      '''

(x, y) = (0, 100)
guessNum = (y - x)/2 + x
print 'I guess the number is:',guessNum
while True:
    entHint = raw_input('Enter the hint:')
    if entHint == 'yes':
        print 'I guessed'
        break
    elif entHint == 'big':
        y = guessNum
        guessNum = (y - x)/2 + x
        print 'The number is',guessNum

    elif entHint == 'small':
        x = guessNum
        guessNum = (y - x)/2 + x
        print x
        print 'The number is', guessNum
    else:
        print 'Please enter "small", "big" or"yes"'
