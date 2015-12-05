#!/bin/bash

# Advent of Code 2015
#
# Day 2: I Was Told There Would Be No Math
#
# Giacomo Boccardo 2015

# Part 1
perl -Fx -lane '@w=sort{$a<=>$b} @F; $tot+=3*@w[0]*@w[1]+2*(@w[0]*@w[2]+@w[1]*@w[2]); print $tot if eof' input.txt

# Part 2
perl -Fx -lane '@w=sort{$a<=>$b} @F; $tot+=2*(@w[0]+@w[1])+@w[0]*@w[1]*@w[2]; print $tot if eof' input.txt

