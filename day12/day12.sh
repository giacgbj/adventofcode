#!/bin/bash

# Advent of Code 2015
#
# Day 12: JSAbacusFramework.io
#
# Giacomo Boccardo 2015

# Part 1 - Extremely slow (~20/25m)
# ./day12.sh input.txt
s=$(<$1)
echo $((${s//[^-0-9]/+}0))
# 119433