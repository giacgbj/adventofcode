#!/usr/bin/env python

# Advent of Code 2015
#
# Day 11: Corporate Policy
#
# Giacomo Boccardo 2015

import re

password = "hepxcrrq"

is_valid = False

for n in range(1, 3):
    while not is_valid:
        password_reverted = list(password)[::-1]

        i = 0
        for c in password_reverted:
            password_reverted[i] = chr((ord(c) + 1) % 97 % 26 + 97)
            if c != 'z':
                break
            i += 1

        password = ''.join(password_reverted[::-1])

        if re.match('[iol]', password) or len(re.findall(r'(.)\1+', password)) < 2 or not (any(
                        ord(password[i + 1]) == ord(password[i]) + 1 and ord(password[i + 2]) == ord(password[i]) + 2
                        for i in xrange(0, len(password) - 2))):
            continue

        is_valid = True
    is_valid = False
    print("Part %d: %s" % (n, password))

# Part 1: hepxxyzz
# Part 2: heqaabcc
