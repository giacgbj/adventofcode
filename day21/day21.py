# !/usr/bin/env python

# Advent of Code 2015
#
# Day 21: RPG Simulator 20XX
#
# Giacomo Boccardo 2015

from itertools import combinations
from math import ceil

shopLines = open("inputShop.txt").readlines()
weapons = [list(map(int, line.split()[1:])) for line in shopLines[1:6]]
armor = [list(map(int, line.split()[1:])) for line in shopLines[8:13]]
rings = [list(map(int, line.split()[2:])) for line in shopLines[15:]]

# "Armor is optional, but you can't use more than one"
armor.append([0, 0, 0])

# "You can buy 0-2 rings (at most one for each hand)"
rings.extend([[0, 0, 0], [0, 0, 0]])

bossLines = open("input.txt").readlines()
bossHP = int(bossLines[0].split(":")[1])
bossDamage = int(bossLines[1].split(":")[1])
bossArmor = int(bossLines[2].split(":")[1])

playerHP = 100


def boss_damage_per_round(w, r):
    # "An attacker always does at least 1 damage"
    return max(1, w[1] + r[0][1] + r[1][1] - bossArmor)


def player_damage_per_round(a, r):
    # "An attacker always does at least 1 damage"
    return max(1, bossDamage - a[2] - r[0][2] - r[1][2])


print("Part 1: %d" %
      min([w[0] + a[0] + r[0][0] + r[1][0]
           for w in weapons
           for a in armor
           for r in combinations(rings, 2)
           if ceil(bossHP / boss_damage_per_round(w, r)) <= ceil(playerHP / player_damage_per_round(a, r))]))
# 78


print("Part 2: %d" %
      max([w[0] + a[0] + r[0][0] + r[1][0]
           for w in weapons
           for a in armor
           for r in combinations(rings, 2)
           if ceil(bossHP / boss_damage_per_round(w, r)) > ceil(playerHP / player_damage_per_round(a, r))]))
# 148
