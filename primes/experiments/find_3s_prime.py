#!/usr/bin/env python3

"""Find a prime number that requires about 3s to check"""

import sys
from time import perf_counter
import math

from prime import is_prime

try:
    exp = float(sys.argv[1])
except IndexError:
    exp = 50.0

n = int(2 ** exp)
print(n)

while True:
    t0 = perf_counter()
    yes = is_prime(n)
    dt = perf_counter() - t0
    if yes:
        print(f'exp={exp:0.2f} prime={n} time={dt:0.2f}s')
        if dt > 3:
            print(math.log(n, 2))
            break
    exp += 0.01
    n = int(2 ** exp)
