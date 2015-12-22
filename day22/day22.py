# !/usr/bin/env python

# Advent of Code 2015
#
# Day 22: Wizard Simulator 20XX
#
# Giacomo Boccardo 2015

#
# So boring...!!!
#

# id, mana cost, damage, health points, armor, mana, turns duration
missile = (0, 53, 4, 0, 0, 0, 0)
drain = (1, 73, 2, 2, 0, 0, 0)
shield = (2, 113, 0, 0, 7, 0, 6)
poison = (3, 173, 3, 0, 0, 0, 6)
recharge = (4, 229, 0, 0, 0, 101, 5)
spells = [missile, drain, shield, poison, recharge]

bossLines = open("input.txt").readlines()
bossHP = int(bossLines[0].split(":")[1])
bossDamage = int(bossLines[1].split(":")[1])

playerHP = 50
playerMana = 500

leastManaSpent = float('inf')


def evaluate(bossHP, playerHP, playerMana, activeSpells, manaSpent, isPlayerTurn, isPartTwo):
    # "At the start of each player turn (before any other effects apply), you lose 1 hit point."
    if isPartTwo and isPlayerTurn:
        playerHP -= 1
        # "If this brings you to or below 0 hit points, you lose."
        if playerHP <= 0:
            return

    playerArmor = 0
    currActiveSpells = []
    for s in activeSpells:
        # Spell active
        if s[6] >= 0:
            # "Since you do magic damage, your opponent's armor is ignored, and so the boss effectively has zero armor"
            bossHP -= s[2]
            playerHP += s[3]
            playerArmor += s[4]
            playerMana += s[5]

        currActiveSpell = list(s)
        currActiveSpell[6] -= 1

        # Spell still active
        if currActiveSpell[6] > 0:
            currActiveSpells.append(currActiveSpell)

    # Yeah!
    if bossHP <= 0:
        global leastManaSpent
        if manaSpent < leastManaSpent:
            # Fuck yeah!
            leastManaSpent = manaSpent
        return

    # Too much mana used
    if manaSpent >= leastManaSpent:
        return

    if isPlayerTurn:
        for spell in spells:
            currManaCost = spell[1]
            # "You cannot cast a spell that would start an effect which is already active."
            if currManaCost <= playerMana and all(spell[0] != s[0] for s in currActiveSpells):
                newActiveSpellsCopy = list(currActiveSpells)
                newActiveSpellsCopy.append(spell)
                evaluate(bossHP, playerHP, playerMana - currManaCost, newActiveSpellsCopy, manaSpent + currManaCost, False, isPartTwo)
    else:
        # "If armor would reduce damage below 1, it becomes 1 instead - that is, the boss' attacks always deal at least 1 damage."
        playerHP += min(-1, playerArmor - bossDamage)
        if playerHP > 0:
            evaluate(bossHP, playerHP, playerMana, currActiveSpells, manaSpent, True, isPartTwo)


evaluate(bossHP, playerHP, playerMana, [], 0, True, False)
print("Part 1: %d" % leastManaSpent)
# 900

leastManaSpent = float('inf')
evaluate(bossHP, playerHP, playerMana, [], 0, True, True)
print("Part 2: %d" % leastManaSpent)
# 1216
