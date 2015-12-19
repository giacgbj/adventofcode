# !/usr/bin/env python

# Advent of Code 2015
#
# Day 19: Medicine for Rudolph
#
# Giacomo Boccardo 2015

import re

lines = open("input.txt").readlines()

replacements = [re.findall('(\S+) => (\S+)', l)[0] for l in lines[:-2]]
molecule = lines[-1].strip()

distinct_molecules = set()
for left, right in replacements:
    for i in range(len(molecule)):
        if left == molecule[i: i + len(left)]:
            distinct_molecules.add(molecule[:i] + right + molecule[i + len(left):])

print("Part 1: %d" % len(distinct_molecules))
# 535


# All the productions have the following forms:
# α => β γ
# α => β Rn γ Ar
# α => β Rn γ Y δ Ar
# α => β Rn γ Y δ Y ε Ar
#
# "Fortunately", Rns, Ars and Ys are only on the right side of the productions, therefore they do not produce anything, so they can be reduced.
# Moreover, Ys eliminate the respective following elements.
# So, the result can be calculated as the difference between the elements in the input data minus the Rns and the Ars, minus two times the Ys, minus 1 for the starting element "e":
#
# steps = count(initialElements) - count(Rns|Ars) - 2 * count(Ys) - 1
# The initial elements can be easily counted because each one starts with a capital letter ;-)

steps = sum(map(str.isupper, molecule)) - molecule.count("Rn") - molecule.count("Ar") - 2 * molecule.count("Y") - 1
print("Part 2: %d" % steps)
# 212


# Alternative solution (for this particular grammar!)
steps = 0
while molecule != "e":
    for left, right in replacements:
        if right in molecule:
            molecule = molecule.replace(right, left, 1)
            steps += 1

print("Part 2: %d" % steps)
# 212
