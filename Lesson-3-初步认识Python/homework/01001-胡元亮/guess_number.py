# -*- coding: utf-8 -*-

import random

if __name__ == "__main__":
    goal = str(random.randint(1, 100))
    num_input = raw_input("Please type a number: ")
    chances = 5

    while goal != num_input and chances:
        chances -= 1
        s = "smaller" if goal > num_input else "bigger"
        num_input = raw_input("Your number is %s than the target. Please try again: " % s)

    print "Congratulations!" if goal == num_input else "Sorry! The answer is %s." % goal
