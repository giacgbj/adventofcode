#!/bin/bash

# Advent of Code 2015
#
# Day 5: Doesn't He Have Intern-Elves For This?
#
# Giacomo Boccardo 2015

# Part 1
cat input.txt | egrep '([aeiou][^aeiou]*){3}' | egrep '(.)\1' | egrep -v 'ab|cd|pq|xy' | wc -l

# Part 2
cat input.txt | egrep '(..).*\1' | egrep '(.).\1' | wc -l