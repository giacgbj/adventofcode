#!/usr/bin/env python

# Advent of Code 2015
#
# Day 6: Probably a Fire Hazard (Part 1)
#
# Giacomo Boccardo 2015

import re

from PIL import Image

lights = Image.new('RGB', (1000, 1000), 'black')
pixels = lights.load()

grid = [[False for x in range(1000)] for x in range(1000)]
tot_lights_on = 0

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
                prev = grid[x][y]

                if 'n' == action:
                    if not prev:
                        tot_lights_on += 1
                    grid[x][y] = True
                elif 'f' == action:
                    if prev:
                        tot_lights_on -= 1
                    grid[x][y] = False
                elif 'e' == action:
                    tot_lights_on = tot_lights_on - 1 if prev else tot_lights_on + 1
                    grid[x][y] = not prev

                pixels[x, y] = (255, 255, 255) if grid[x][y] else (0, 0, 0)

print('Part 1:', tot_lights_on)
lights.save('day06_1.png')
