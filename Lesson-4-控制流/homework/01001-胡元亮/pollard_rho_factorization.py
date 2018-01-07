# -*- coding: utf-8 -*-

import math
import random
import timeit


def mod_mul(a, b, n):
    result = 0
    while b:
        if b & 1:
            result = (result + a) % n
        a = (a + a) % n
        b >>= 1
    return result


def mod_exp(a, b, n):
    result = 1
    while b:
        if b & 1:
            result = mod_mul(result, a, n)
        a = mod_mul(a, a, n)
        b >>= 1
    return result


def prime_check(number):
    """
    This function uses Miller–Rabin primality test.
    Reference: https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test

    :param number: The integer for testing.
    :return: True if the integer is a prime.
    """
    num_list = [2, 3, 5, 7, 11]
    if number in num_list:
        return True
    if number == 1 or 0 in [number % i for i in num_list]:
        return False

    k, u = 0, number - 1

    while not u & 1:
        k += 1
        u >>= 1

    random.seed(0)
    for i in range(5):
        x = random.randint(2, number - 1)
        if x % number == 0:
            continue
        x = mod_exp(x, u, number)
        pre = x
        for j in range(k):
            x = mod_mul(x, x, number)
            if x == 1 and pre != 1 and pre != number - 1:
                return False
            pre = x
        if x != 1:
            return False
        return True


def gcd(num_a, num_b):
    return gcd(num_b, num_a % num_b) if num_b else num_a


def gen(number):
    return lambda n: (n * n + 1) % number


def get_prime_factors(number, start=2):
    """
    This function is the common way of factorization, which is simple but slow.

    :param number: A positive integer for factorization.
    :param start: Internal use only.
    :return A list containing all the prime factors of the number.
    """
    for prime in range(start, int(math.sqrt(number)+1)):
        if number % prime == 0:
            return [prime] + get_prime_factors(number/prime, prime)

    return [] if number == 1 else [number]


def get_rho_factors(number):
    """
    This function uses a variant Pollard's rho algorithm.
    Note that this algorithm may find factors which are not primes.
    In that case, the method uses the normal factorization: get_prime_factors.
    Reference: https://en.wikipedia.org/wiki/Pollard's_rho_algorithm

    :param number: A positive integer for factorization.
    :return A list containing all the prime factors of the number.
    """
    factor_list = []

    x, y, factor = 2, 2, 1
    while number != 1:
        g = gen(number)
        while factor == 1:
            x = g(x)
            y = g(g(y))
            factor = gcd(y-x, number)
        factor_list += [factor] if prime_check(factor) else get_prime_factors(factor)
        number /= factor
        x, y, factor = 2, 2, 1

    return factor_list


if __name__ == "__main__":
    num = 0
    while num < 2:
        try:
            num = int(raw_input("Enter an integer larger than 1 for analyzing: "))
        except ValueError:
            continue

    start_time = timeit.default_timer()
    factors = " * ".join([str(p) for p in get_rho_factors(num)])
    elapsed_time = timeit.default_timer() - start_time
    print "-" * 80
    print "{num} = {factors}".format(**locals())
    print "%8f seconds elapsed during calculation." % elapsed_time
    print "-" * 80
