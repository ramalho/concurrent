#!/usr/bin/env python3

# source:
# https://codereview.stackexchange.com/questions/121862/fast-number-factorization-in-python

import itertools


def prime_factors(n):
    for i in itertools.chain([2], itertools.count(3, 2)):
        if n <= 1:
            break
        while n % i == 0:
            n //= i
            yield i


def main():
    from time import perf_counter

    prime = 3033700317376073
    n = prime - 2
    t0 = perf_counter()
    factors = list(prime_factors(n))
    dt = perf_counter() - t0
    print(n, f'{dt:0.3f}s', factors)


if __name__ == '__main__':
    main()
