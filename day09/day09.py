#!/usr/bin/env python

# Advent of Code 2015
#
# Day 9: All in a Single Night
#
# Giacomo Boccardo 2015

import re
from itertools import permutations

edges = {}
nodes = set()

for source, dest, distance in re.findall('(\S+) to (\S+) = (\d+)', open("input.txt").read()):
    edges[source, dest] = edges[dest, source] = int(distance)
    nodes.add(source)
    nodes.add(dest)

print min(sum(edges[a, b] for a, b in zip(p, p[1:])) for p in permutations(nodes))
# 141

print max(sum(edges[a, b] for a, b in zip(p, p[1:])) for p in permutations(nodes))
# 736
