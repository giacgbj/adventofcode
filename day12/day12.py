#!/usr/bin/env python

# Advent of Code 2015
#
# Day 12: JSAbacusFramework.io
#
# Giacomo Boccardo 2015

import json
import re

print("Part 1: %d" % sum(map(int, re.findall('-?\d+', open("input.txt").read()))))
# 119433


def sum_without_reds(s):
    if isinstance(s, dict):
        return 0 if "red" in s.values() else sum(map(sum_without_reds, s.values()))
    elif isinstance(s, list):
        return sum(map(sum_without_reds, s))
    elif isinstance(s, int):
        return s
    return 0


print("Part 2: %d" % sum_without_reds(json.load(open("input.txt"))))
# 68466
