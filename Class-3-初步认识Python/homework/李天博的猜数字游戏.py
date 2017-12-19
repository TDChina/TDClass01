
import random

secret = random.randint(1,100)

#print(secret)

print('------welcome to play this game-----')

guess = 0

while guess != secret:

    temp = input('Please input your guess number:')

    guess = int(temp)

    if guess > secret:

        print('Your guess is too high!')

    else:

        print('Your guess is too low!')

if guess == secret:

    print('Congratulations to you! Your  guess is right!')

    print('Game over, Goodbye!')