# !/usr/bin/env python

# Advent of Code 2015
#
# Day 25: Let It Snow
#
# Giacomo Boccardo 2015

# Quite easy...

start = 20151125
factor = 252533
divisor = 33554393

row = 2947
col = 3029

codePosition = (row + col) * (row + col - 1) // 2 - row + 1

code = start
for i in range(codePosition-1):
    code = (code * factor) % divisor

print("That's all, folks: %d" % code)
# 19980801
