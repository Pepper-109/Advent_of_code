# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 16:11:29 2023

@author: Alix
"""

# ----------------------------- Part 1 -----------------------------

print("----------------------------- Part 1 -----------------------------")

'''
Picking one up, it looks like each card has two lists of numbers
separated by a vertical bar (|):
    a list of winning numbers and then
    a list of numbers you have.

As far as the Elf has been able to figure out,
you have to figure out which of the numbers you have appear
in the list of winning numbers.

The first match makes the card worth one point,
each match after the first doubles the point value of that card.
'''

with open("input.txt", 'r') as file:
    card_value_sum = 0

    for line in file.readlines():
        line = line.strip().split(": ")[1]
        line = line.split(" | ")

        winning = [int(num) for num in line[0].split(' ') if len(num) != 0]
        elf_num = [int(num) for num in line[1].split(' ') if len(num) != 0]

        card_value = 0

        for num in elf_num:
            if num in winning:
                if card_value == 0:
                    card_value = 1
                else:
                    card_value *= 2

        card_value_sum += card_value

print("The elf's pile of scratchcards are worth:", card_value_sum)


# ----------------------------- Part 2 -----------------------------

print("----------------------------- Part 2 -----------------------------")

'''
There's no such thing as "points".

Instead, scratchcards only cause you to win more scratchcards
equal to the number of winning numbers you have.

Specifically, you win copies of the scratchcards below the winning card equal
to the number of matches.

So, if card 10 were to have 5 matching numbers,
you would win one copy each of cards 11, 12, 13, 14, and 15.

Copies of scratchcards are scored as normal and have the same card number
as the card they copied.

So, if you win a copy of card 10 and it has 5 matching numbers,
it would then win a copy of the same cards that the original card 10 won:
cards 11, 12, 13, 14, and 15.

This process repeats until none of the copies cause you to win any more cards.
'''

with open("input.txt", 'r') as file:
    scratch_card_count = 0
    scratch_cards = {}

    for line in file.readlines():
        line = line.strip().split(": ")
        card = int(line[0].split("Card ")[1])
        numbers = line[1].split(" | ")

        winning = [int(num) for num in numbers[0].split(' ') if len(num) != 0]
        elf_num = [int(num) for num in numbers[1].split(' ') if len(num) != 0]

        copies_to_create = []  # Keep track of which cards to copy
        instances = 1

        for num in elf_num:
            if num in winning:
                if len(copies_to_create) == 0:
                    copies_to_create = [card + 1]
                else:
                    copies_to_create.append(copies_to_create[-1] + 1)

        scratch_cards[card] = [winning, elf_num, copies_to_create, instances]

    for card, card_info in scratch_cards.items():
        # Copy each card in the copy list
        for copy in card_info[2]:
            # Create another "num of current card" copies of a card.
            # Isn't recursion fun...
            scratch_cards[copy][3] = scratch_cards[copy][3] + card_info[3]

    for scratch_card in scratch_cards.items():
        scratch_card_count += scratch_card[-1][-1]

print("The elf's pile of scratchcards is:", scratch_card_count, "cards high.")
