# !/usr/bin/env python

# Advent of Code 2015
#
# Day 18: Like a GIF For Your Yard
#
# Giacomo Boccardo 2015

steps = 100
grid_width = 100
grid_height = 100


def evaluate_lights_on(lights_always_on):
    with open('input.txt') as f:
        lights_on = {(x, y) for y, line in enumerate(f) for x, char in enumerate(line.strip()) if '#' == char}
        lights_on |= lights_always_on

    def count_neighbors_on(x, y):
        return sum((xx, yy) in lights_on for xx in range(x - 1, x + 2) for yy in range(y - 1, y + 2) if (xx, yy) != (x, y))

    for _ in range(steps):
        lights_on = {(x, y) for x in range(grid_width) for y in range(grid_height)
                     if
                     (x, y) in lights_on and count_neighbors_on(x, y) in (2, 3)
                     or
                     (x, y) not in lights_on and count_neighbors_on(x, y) == 3}
        lights_on |= lights_always_on

    return lights_on


print("Part 1: %d" % len(evaluate_lights_on(set())))
# 821

corners_always_on = {(0, 0), (0, 99), (99, 0), (99, 99)}
print("Part 2: %d" % len(evaluate_lights_on(corners_always_on)))
# 886
