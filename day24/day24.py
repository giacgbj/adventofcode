# !/usr/bin/env python

# Advent of Code 2015
#
# Day 24: It Hangs in the Balance
#
# Giacomo Boccardo 2015

from itertools import combinations
from operator import mul
from functools import reduce

weights = [int(line) for line in open("input.txt")]


def evaluate(numberOfGroups):
    # Each group must have exactly the sum of the weights divided by the number of groups
    weightPerGroup = sum(weights) // numberOfGroups
    return evaluateRec(weightPerGroup, weights, numberOfGroups, numberOfGroups)


# The idea is to test all the combinations of increasing weights' groups' sizes.
# When the sum of the weights of a group equals the required weight, the remaining weights must be tested calling the function recursively
# until the number of groups to verify equals 2 (if a group has the required weight the other one has obviously the same weight).
# Multiplying by each other the weights of the chosen group, the quantum entanglement is obtained.
def evaluateRec(weightPerGroup, currWeights, numberOfGroups, groupsToCheck):
    for packagesPerGroup in range(1, len(currWeights)):
        for currGroup in (c for c in combinations(currWeights, packagesPerGroup) if weightPerGroup == sum(c)):
            if groupsToCheck == 2:
                return True
            elif groupsToCheck < numberOfGroups:
                return evaluateRec(weightPerGroup, list(set(currWeights) - set(currGroup)), numberOfGroups, groupsToCheck - 1)
            elif evaluateRec(weightPerGroup, list(set(currWeights) - set(currGroup)), numberOfGroups, groupsToCheck - 1):
                return reduce(mul, currGroup, 1)

print("Part 1: %d" % evaluate(3))
# 11266889531

print("Part 2: %d" % evaluate(4))
# 77387711
