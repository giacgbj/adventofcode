# !/usr/bin/env python

# Advent of Code 2015
#
# Day 20: Infinite Elves and Infinite Houses
#
# Giacomo Boccardo 2015

import functools
import operator
from itertools import product
from math import sqrt
from timeit import default_timer as timer

from primefac import factorint

input = 36000000
input_div_10 = input / 10
input_div_11 = input / 11
part_2_house_limit = 50


def sqrt_upper_bound(n):
    return set(x for t in ([i, n // i] for i in range(1, int(sqrt(n)) + 1) if n % i == 0) for x in t)


# The factors of odd numbers are always odd, so...
def parity_check(n):
    step = 2 if n % 2 else 1
    return set(x for t in ([i, n // i] for i in range(1, int(sqrt(n)) + 1, step) if n % i == 0) for x in t)


def with_divmod(n):
    result = set()
    for i in range(1, int(sqrt(n)) + 1):
        div, mod = divmod(n, i)
        if mod == 0:
            result |= {i, div}
    return result


def divmod_with_parity_check(n):
    result = set()
    step = 2 if n % 2 else 1
    for i in range(1, int(sqrt(n)) + 1, step):
        div, mod = divmod(n, i)
        if mod == 0:
            result |= {i, div}
    return result


def primefac_library(n):
    primes_and_exps = factorint(n)
    values = [[(f ** e) for e in range(exp + 1)] for (f, exp) in primes_and_exps.iteritems()]
    return set(functools.reduce(operator.mul, v, 1) for v in product(*values))


funcs = [sqrt_upper_bound, parity_check, with_divmod, divmod_with_parity_check, primefac_library]

for f in funcs:
    start = timer()
    house = 1
    part_1 = part_2 = None

    while not (part_1 and part_2):
        house += 1

        divisors = f(house)

        if not part_1 and sum(divisors) >= input_div_10:
            part_1 = house

        if not part_2 and sum(d for d in divisors if house / d <= part_2_house_limit) >= input_div_11:
            part_2 = house

    print("Part 1/2 (using %s): %d/%d (%s)" % (f.__name__, part_1, part_2, timer() - start))
    # 831600/884520
