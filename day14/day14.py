#!/usr/bin/env python

# Advent of Code 2015
#
# Day 14: Reindeer Olympics
#
# Giacomo Boccardo 2015

import re
import math

s = 2503

dists = []

for v, flyTime, restTime in re.findall('.+?(\d+).+?(\d+).+?(\d+).+?', open("input.txt").read()):
    flyTime = float(flyTime)
    restTime = float(restTime)
    totTime = flyTime + restTime
    v = float(v)
    dist = (math.floor(s / totTime) * flyTime + min(s % totTime, flyTime)) * v
    dists.append(dist)

print("Part 1: %d" % max(dists))
# 2640
