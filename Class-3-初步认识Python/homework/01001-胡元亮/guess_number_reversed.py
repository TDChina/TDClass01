# -*- coding: utf-8 -*-

import random
from __builtin__ import raw_input

if __name__ == "__main__":
    num_min, num_max = 1, 100
    guess = random.randint(num_min, num_max)
    result = raw_input("I guess the number is %s, is that correct? [Y/B/S] " % guess)
    
    while not result in ["y", "Y"]:
        if result in ["b", "B"] and max > guess:
            num_max = guess - 1
        elif result in ["s", "S"] and min < guess:
            num_min = guess + 1
        
        guess = random.randint(num_min, num_max)
        result = raw_input("I guess the number is %s, is that correct? [Y/B/S] " % guess)
        
    print "Yahoo!"