#!/usr/bin/env python

# Advent of Code 2015
#
# Day 8: Matchsticks
#
# Giacomo Boccardo 2015

from re import escape

with open("input.txt") as f:
    lines = f.readlines()

    tot1 = 0
    tot2 = 0
    for line in lines:
        line = line.strip()
        lineLength = len(line)

        tot1 += lineLength
        tot1 -= len(eval(line))

        tot2 -= lineLength
        tot2 += len(escape(line)) + 2

print("Part 1:", tot1)
# 1350

print("Part 2:", tot2)
# 2085


# Shorter and improved versions (no need to escape in Part 2, conceptually similar to Bash/sed version)

print("Part 1:", sum(len(l.strip()) - len(eval(l)) for l in open("input.txt")))
# 1350

print("Part 2:", sum(l.count('\\') + l.count('"') + 2 for l in open("input.txt")))
# 2085