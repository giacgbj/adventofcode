#!/usr/bin/env python

# Advent of Code 2015
#
# Giacomo Boccardo 2015

moves = {'^': (0, 1), '>': (1, 0), 'v': (0, -1), '<': (-1, 0)}

def reached_houses(path):
    prev_house = (0, 0)
    houses = set([prev_house])
    for move in path:
        curr_house = tuple(map(sum, zip(prev_house, moves[move])))
        houses.add(curr_house)
        prev_house = curr_house
    return houses

with open('input.txt') as f:
    path = f.read()

    houses = reached_houses(path)
    print('Part 1:', len(houses))

    santa_houses = reached_houses(path[::2])
    robot_santa_houses = reached_houses(path[1::2])
    print('Part 2:', len(santa_houses | robot_santa_houses))
