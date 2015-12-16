#!/bin/bash

# Advent of Code 2015
#
# Day 16: Aunt Sue
#
# Giacomo Boccardo 2015

# Part 1
while read l; do grep "$l" input.txt; done < message.txt | sed 's/Sue \([0-9]*\)*.*/\1/' | sort | uniq -c | sort | tail -1 | awk '{print $2}'
#40