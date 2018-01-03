# coding=utf8
# Copyright (c) 2017 CineUse



import random
 secret = random.randint(1,100)
 time = 10
 guess = 0
  print("------welcome to the place where you can guess the Numbers, please start-----")
  while guess != secret and time >= 10:
     guess = int(input("Please input your guess number:"))
     print ("your input number :",guess)
     if guess == secret
         print ("Good,you guessed it")
     else:
     if guess > secret:
         print("Your guess is too high!")
     else:
         print("Your guess is too low!")
         print("Sorry, you are wrong, You have",time,"opportunit")
     time-= 1
         print("Game over, Goodbye!")

