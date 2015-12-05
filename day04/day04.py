#!/usr/bin/env python

# Advent of Code 2015
#
# Day 4: The Ideal Stocking Stuffer
#
# Giacomo Boccardo 2015

import hashlib

secret_key = "yzbqklnj"


def find_lowest_positive_number(zeros):
    lowest_positive_number = -1
    md5 = ""
    while not md5.startswith("0" * zeros):
        lowest_positive_number += 1
        md5 = hashlib.md5((secret_key + str(lowest_positive_number)).encode('utf-8')).hexdigest()
    return lowest_positive_number


print("Part 1:", find_lowest_positive_number(5))

print("Part 2:", find_lowest_positive_number(6))

