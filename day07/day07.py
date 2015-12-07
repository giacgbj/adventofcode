#!/usr/bin/env python

# Advent of Code 2015
#
# Day 7: Some Assembly Required
#
# Giacomo Boccardo 2015

import re

with open("input.txt") as f:
    lines = f.readlines()

    dict = {}

    while not ("a" in dict and dict["a"] is not None):
        for line in lines:
            m = re.search('([a-z0-9]+)? ?([A-Z]+)? ?(\S*) -> (\S+)', line)

            x = m.group(1)
            op = m.group(2)
            y = m.group(3)
            res = m.group(4)

            if x is not None:
                if x.isdigit():
                    x = int(x)
                else:
                    x = dict[x] if x in dict else None

            if y is not None:
                if y.isdigit():
                    y = int(y)
                else:
                    y = dict[y] if y in dict else None

            if op == 'NOT':
                if y is None:
                    continue
                dict[res] = ~y
            elif op == 'AND':
                if x is None or y is None:
                    continue
                dict[res] = x & y
            elif op == 'OR':
                if x is None or y is None:
                    continue
                dict[res] = x | y
            elif op == 'LSHIFT':
                if x is None or y is None:
                    continue
                dict[res] = x << y
            elif op == 'RSHIFT':
                if x is None or y is None:
                    continue
                dict[res] = x >> y
            elif op is None:
                if x is None:
                    continue
                dict[res] = x;

print("Result:", dict['a'])
# 3176

# For Part 2 just change the input file: 3176 -> b instead of 44430 -> b
# 14710
