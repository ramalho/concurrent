#!/usr/bin/env python3

# source:
# https://codereview.stackexchange.com/questions/121862/fast-number-factorization-in-python

import sys


def is_prime(n):
    if n < 3 or n % 2 == 0:
        return n == 2
    else:
        return not any(n % i == 0 for i in range(3, int(n ** 0.5 + 2), 2))


def main():
    from time import perf_counter

    n = 3033700317376073
    t0 = perf_counter()
    result = is_prime(n)
    dt = perf_counter() - t0
    print(n, result, dt)


if __name__ == '__main__':
    main()
