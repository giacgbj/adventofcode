# !/usr/bin/env python

# Advent of Code 2015
#
# Day 17: No Such Thing as Too Much
#
# Giacomo Boccardo 2015

from itertools import combinations
from collections import defaultdict
from timeit import default_timer as timer

containers = [int(line) for line in open("input.txt").readlines()]

start = timer()

tot = 0
counter = defaultdict(int)
for i in range(len(containers)):
    for c in combinations(containers, i):
        if 150 == sum(c):
            tot += 1
            counter[len(c)] += 1

print("Part 1: %d (%s)" % (tot, timer() - start))
# 4372 (~0.35s)

print("Part 2: %d" % counter[min(counter.keys())])