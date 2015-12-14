#!/usr/bin/env python

# Advent of Code 2015
#
# Day 14: Reindeer Olympics
#
# Giacomo Boccardo 2015

import math
import re
from collections import Counter
from itertools import accumulate, cycle

s = 2503

dists = []

for v, flyTime, restTime in re.findall('.+?(\d+).+?(\d+).+?(\d+).+?', open("input.txt").read()):
    flyTime = int(flyTime)
    restTime = int(restTime)
    totTime = flyTime + restTime
    v = int(v)
    dist = (math.floor(s / totTime) * flyTime + min(s % totTime, flyTime)) * v
    dists.append(dist)

print("Part 1: %d" % max(dists))
# 2640

############################################

# Part 2: short version

path = {}

for reindeer, v, flyTime, restTime in re.findall('(\w+).+?(\d+).+?(\d+).+?(\d+).+?', open("input.txt").read()):
    flyTime = int(flyTime)
    restTime = int(restTime)
    totTime = flyTime + restTime
    v = int(v)
    pattern = cycle(flyTime * [v] + restTime * [0])
    path[reindeer] = list(accumulate(next(pattern) for _ in range(s)))

print("Part 2: %d" % max(Counter([index for dists_at_second in zip(*path.values()) for index, dist in enumerate(dists_at_second) if max(dists_at_second) == dist]).values()))
# 1102

############################################

# Part 2: short version, more readable and, somehow, explained

for reindeer, v, flyTime, restTime in re.findall('(\w+).+?(\d+).+?(\d+).+?(\d+).+?', open("input.txt").read()):
    flyTime = int(flyTime)
    restTime = int(restTime)
    totTime = flyTime + restTime
    v = int(v)

    # Test can fly 10 km/s for 5 seconds, but then must rest for 3 seconds.
    # [10, 10, 0, 0, 0] U [10, 10, 0, 0, 0] … [10, 10, 0, 0, 0] … +inf
    pattern = cycle(flyTime * [v] + restTime * [0])

    #   [10, 10+10, 10+10+0, 10+10+0+0, 10+10+0+0+0, 10+10+0+0+0+10, 10+10+0+0+0+10+10, 10+10+0+0+0+10+10+0, ...] =
    # = [10, 20, 20, 20, 20, 30, 40, 40, ...]
    path[reindeer] = list(accumulate(next(pattern) for _ in range(s)))


indexes = []

# For each second, the list of distances the reindeers traveled until that very second...
for dists_at_second in zip(*path.values()):
    # ...for each distance, keeping track of the index (~= the reindeer) in the list, ...
    for index, dist in enumerate(dists_at_second):
        # ...if it's equal to the maximum distance traveled until that very second...
        if max(dists_at_second) == dist:
            # ...save the index of the reindeer in an array
            indexes.append(index)


# Get the maximum value after having counted/grouped the occurrences of the indexes
print("Part 2: %d" % max(Counter(indexes).values()))
# 1102
