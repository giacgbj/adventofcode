#!/usr/bin/env python

# Advent of Code 2015
#
# Day 16: Aunt Sue
#
# Giacomo Boccardo 2015

import re

message = {"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, "akitas": 0, "vizslas": 0, "goldfish": 5,
           "trees": 3, "cars": 2, "perfumes": 1}

# Part 1 and 2 using sets
messageSet = set(message.items())
for n, clue1, clue1q, clue2, clue2q, clue3, clue3q in re.findall('.+?(\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)',
                                                                 open("input.txt").read()):
    clue1q = int(clue1q)
    clue2q = int(clue2q)
    clue3q = int(clue3q)
    cluesMap = {clue1: clue1q, clue2: clue2q, clue3: clue3q}

    cluesSet = set(cluesMap.items())
    if cluesSet.issubset(messageSet):
        print("Part 1: %s" % n)

    # Idea: check the "<" and ">" conditions, removing their values from the each test set
    # in order to test the "=" conditions looking for a subset.
    # I used pop's default value as a trick to avoid testing for non existing elements.
    if message["cats"] < cluesMap.pop("cats", message["cats"] + 1) and message["trees"] < cluesMap.pop("trees", message[
        "trees"] + 1) and message["pomeranians"] > cluesMap.pop("pomeranians", -1) and message[
        "goldfish"] > cluesMap.pop("goldfish", -1):
        cluesSet = set(cluesMap.items())
        if cluesSet.issubset(messageSet):
            print("Part 2: %s" % n)


# Part 1/2, more verbose and easier to understand
for n, clue1, clue1q, clue2, clue2q, clue3, clue3q in re.findall(
        '.+?(\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)',
        open("input.txt").read()):
    clue1q = int(clue1q)
    clue2q = int(clue2q)
    clue3q = int(clue3q)

    if message[clue1] == clue1q and message[clue2] == clue2q and message[clue3] == clue3q:
        print("Part 1: %s" % n)
        # 40

    cluesMap = {clue1: clue1q, clue2: clue2q, clue3: clue3q}
    found = 0

    for k, v in cluesMap.items():
        if k in ("cats", "trees") and message[k] < cluesMap[k]:
            found += 1
        elif k in ("pomeranians", "goldfish") and message[k] > cluesMap[k]:
            found += 1
        elif k not in ("cats", "trees", "pomeranians", "goldfish") and message[k] == cluesMap[k]:
            found += 1
    if found == 3:
        print("Part 2: %s" % n)
        # 241
