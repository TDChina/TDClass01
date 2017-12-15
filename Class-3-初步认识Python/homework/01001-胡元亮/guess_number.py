# -*- coding: utf-8 -*-

import random
from __builtin__ import raw_input

if __name__ == "__main__":
    goal = str(random.randint(1, 100))
    num_input = raw_input("Please type a number: ")
    
    while goal != num_input:
        s = "smaller" if goal > num_input else "bigger"
        num_input = raw_input("Your number is %s than the target. Please try again: " % s)
        
    print "Congratulations!"
