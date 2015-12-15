#!/usr/bin/env python

# Advent of Code 2015
#
# Day 15: Science for Hungry People
#
# Giacomo Boccardo 2015

import re
from functools import reduce
from operator import mul
from numpy import array

spoons = 100

ingrs_and_cals = array([list(map(int, re.findall('-?\d+', line))) for line in open("input.txt").readlines()])

tots = []
for a in range(spoons + 1):
    for b in range(spoons + 1 - a):
        for c in range(spoons + 1 - a - b):
            d = spoons - a - b - c
            tot_ingrs = reduce(mul, map(lambda *x: max(0, sum(x)), *map(mul, [a, b, c, d], ingrs_and_cals[:, :-1])))
            tot_cals = sum(map(mul, [a, b, c, d], ingrs_and_cals[:, -1]))
            tots.append((tot_ingrs, tot_cals))

print("Part 1: %d" % max(s[0] for s in tots))
# 13882464

print("Part 2: %d" % max(s[0] for s in tots if 500 == s[1]))
# 11171160
