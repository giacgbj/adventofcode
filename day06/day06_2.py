#!/usr/bin/env python

# Advent of Code 2015
#
# Day 6: Probably a Fire Hazard (Part 2)
#
# Giacomo Boccardo 2015

import re

grid = [[0 for x in range(1000)] for x in range(1000)]
tot_brightness = 0

with open("input.txt") as f:
    lines = f.readlines()

    for line in lines:
        m = re.search('([a-z])\s(\d+),(\d+)[a-z\s]+(\d+),(\d+)', line)

        action = m.group(1)
        x1 = int(m.group(2))
        y1 = int(m.group(3))
        x2 = int(m.group(4))
        y2 = int(m.group(5))

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if 'n' == action:
                    tot_brightness += 1
                    grid[x][y] += 1
                elif 'f' == action:
                    if grid[x][y] != 0:
                        tot_brightness -= 1
                        grid[x][y] -= 1
                elif 'e' == action:
                    tot_brightness += 2
                    grid[x][y] += 2

print('Part 2:', tot_brightness)
