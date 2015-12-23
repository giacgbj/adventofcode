# !/usr/bin/env python

# Advent of Code 2015
#
# Day 23: Opening the Turing Lock
#
# Giacomo Boccardo 2015

import re

ins = [m for m in re.findall('(\w+) ?(\w)?,? ?([-\+]\d+)?', open('input.txt').read())]


def evaluate(regs):
    i = 0
    while 0 <= i < len(ins):
        op, reg, offset = ins[i]

        if op == 'hlf':
            regs[reg] //= 2
        elif op == 'tpl':
            regs[reg] *= 3
        elif op == 'inc':
            regs[reg] += 1
        elif op == 'jmp' or op == 'jie' and regs[reg] % 2 == 0 or op == 'jio' and regs[reg] == 1:
            i += int(offset)
            continue

        i += 1
    return regs


print("Part 1: %d" % evaluate({'a': 0, 'b': 0})['b'])
# 255

print("Part 2: %d" % evaluate({'a': 1, 'b': 0})['b'])
# 334
