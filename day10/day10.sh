#!/bin/bash

# Advent of Code 2015
#
# Day 10: Elves Look, Elves Say
#
# Giacomo Boccardo 2015

# $ day10.sh 3113322113 40
# 329356

# $ day10.sh 3113322113 50
# 4666278

res=$1
steps=$2

for i in `seq $steps`;
do
    # Shorter and shorter...
    # res=$(echo $res | grep -o . | uniq -c | tr -d '\n ')
    # res=$(echo $res | fold -w1 | uniq -c | tr -d '\n ')
      res=`fold -w1 <<< $res | uniq -c | tr -d '\n '`
done

# Not short enough!
# echo -n $res | wc -c

# Technically, in prints the result (and something else...I'm a very bad person ;-))
${#res}
