#!/bin/bash

# Advent of Code 2015
#
# Day 1: Not Quite Lisp
#
# Giacomo Boccardo 2015

# Part 1
expr `grep -o \( input.txt | wc -l` - `grep -o \) input.txt | wc -l`

# Part 2
awk -v FS="" '{ for(i=1; i<=NF; i++) { tot+= $i=="(" ? 1 : -1; if (tot<0) { print i; break; } } }' input.txt