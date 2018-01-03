# -*- coding: utf-8 -*-

import math
import timeit


def get_prime_factors(number, start=2):
    """
    :param number: A positive integer for factorization.
    :param start: Internal use only.
    :return A list containing all the prime factors of the number.
    """
    for prime in range(start, int(math.sqrt(number)+1)):
        if number % prime == 0:
            return [prime] + get_prime_factors(number/prime, prime)

    return [] if number == 1 else [number]


if __name__ == "__main__":
    num = 0
    while num < 2:
        try:
            num = int(raw_input("Enter an integer larger than 1 for analyzing: "))
        except ValueError:
            continue

    start_time = timeit.default_timer()
    factors = " * ".join([str(p) for p in get_prime_factors(num)])
    elapsed_time = timeit.default_timer() - start_time
    print "-" * 80
    print "{num} = {factors}".format(**locals())
    print "%8f seconds elapsed during calculation." % elapsed_time
    print "-" * 80
