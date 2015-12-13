#!/usr/bin/env python

# Advent of Code 2015
#
# Day 13: Knights of the Dinner Table
#
# Giacomo Boccardo 2015

import re
from itertools import permutations

edges = {}
nodes = set()

for a, op, happiness, b in re.findall('(\w+).+(\w) (\d+).+?(\w+)\.', open("input.txt").read()):
    edges[a, b] = int(happiness) * (-1 if op == "e" else 1)
    edges[a, "Giacomo"] = edges["Giacomo", a] = 0
    nodes.add(a)

print("Part 1:", max(sum(edges[a, b] + edges[b, a] for a, b in zip(p, p[1:] + p[:1])) for p in permutations(nodes)))
# 733

nodes.add("Giacomo")
print("Part 2:", max(sum(edges[a, b] + edges[b, a] for a, b in zip(p, p[1:] + p[:1])) for p in permutations(nodes)))
# 725
