# -*- coding: utf-8 -*-

import random

if __name__ == "__main__":
    num_min, num_max = 1, 100
    result, guess = "", 0

    while result not in ["y", "Y"]:

        if result in ["b", "B"]:
            num_max = max(guess - 1, num_min)
        elif result in ["s", "S"]:
            num_min = min(guess + 1, num_max)

        guess = random.randint(num_min, num_max)
        result = raw_input("I guess the number is %s, is that correct? [Y/B/S] " % guess)

    print "Yahoo!"
