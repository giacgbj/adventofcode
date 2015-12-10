#!/usr/bin/env python

# Advent of Code 2015
#
# Day 10: Elves Look, Elves Say
#
# Giacomo Boccardo 2015

import re

start= "3113322113"

def look_and_say_nth_value(start, steps):
    res = start
    for _ in range(steps):
        res = re.sub(r'(.)\1*', lambda x: str(len(x.group(0))) + x.group(1), res)
    return res


print("Part 1: ", len(look_and_say_nth_value(start, 40)))
#329356

print("Part 2: ", len(look_and_say_nth_value(start, 50)))
#4666278
