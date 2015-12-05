#!/usr/bin/env python

# Advent of Code 2015
#
# Day 5: Doesn't He Have Intern-Elves For This?
#
# Giacomo Boccardo 2015

import re

with open("input.txt") as f:
    lines = f.readlines()

    nice_strings = 0
    for line in lines:
        if re.search('([aeiou].*){3}', line) and re.search(r"(.)\1", line) and not re.search('ab|cd|pq|xy', line):
            nice_strings += 1

    print("Part 1:", nice_strings)

    nice_strings = 0
    for line in lines:
        if re.search(r"(..).*\1", line) and re.search(r"(.).\1", line):
            nice_strings += 1
    print("Part 2:", nice_strings)
