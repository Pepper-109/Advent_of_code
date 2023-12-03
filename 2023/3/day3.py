# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 12:48:23 2023

@author: Alix
"""

# ----------------------------- Part 1 -----------------------------

'''
any number adjacent to a symbol, even diagonally,
is a "part number" and should be included in your sum.

(Periods (.) do not count as a symbol.)

What is the sum of all of the part numbers in the engine schematic?
'''

with open("input.txt", 'r') as file:
    numbers = []
    symbols = []
    current_num = ['', []]
    part_sum = 0

    for row, line in enumerate(file.readlines()):
        line = line.strip()

        for col, char in enumerate(line):
            if char.isnumeric():
                current_num[0] = current_num[0] + char
                current_num[1].append([row, col])
            else:
                # Make sure we're tracking a num
                if len(current_num[0]) != 0:
                    current_num[0] = int(current_num[0])
                    numbers.append(current_num)
                    current_num = current_num = ['', []]

                # Symbol check
                if char != '.':
                    valid_coords = []

                    # Record adjacent coords to the symbol
                    for x in range(row - 1, row + 2):
                        for y in range(col - 1, col + 2):
                            valid_coords.append([x, y])

                    symbols.append([char, valid_coords])

    # Compare all number coords to valid symbol coords
    for symbol, sym_coord in symbols:
        for num, num_coords in numbers:
            for coord in num_coords:
                if coord in sym_coord:
                    part_sum += num
                    break

    print("Part sum:", part_sum)

# ----------------------------- Part 2 -----------------------------

'''
The missing part wasn't the only issue -
one of the gears in the engine is wrong.

A gear is any * symbol that is adjacent to exactly two part numbers.
Its gear ratio is the result of multiplying those two numbers together.

What is the sum of all of the gear ratios in your engine schematic?
'''

with open("input.txt", 'r') as file:
    numbers = []
    symbols = []
    current_num = ['', []]
    gear_ratio = 0

    for row, line in enumerate(file.readlines()):
        line = line.strip()

        for col, char in enumerate(line):
            if char.isnumeric():
                current_num[0] = current_num[0] + char
                current_num[1].append([row, col])
            else:
                # Make sure we're tracking a num
                if len(current_num[0]) != 0:
                    current_num[0] = int(current_num[0])
                    numbers.append(current_num)
                    current_num = current_num = ['', []]

                # Symbol check
                if char != '.':
                    valid_coords = []

                    # Record adjacent coords to the symbol
                    for x in range(row - 1, row + 2):
                        for y in range(col - 1, col + 2):
                            valid_coords.append([x, y])

                    symbols.append([char, valid_coords])

    # Compare all number coords to valid symbol coords
    # Keep track of * symbols and adjacent part numbers
    for symbol, sym_coord in symbols:
        if symbol == '*':
            adj_parts = []

            for num, num_coords in numbers:
                for coord in num_coords:
                    if coord in sym_coord:
                        adj_parts.append(num)
                        break

            if len(adj_parts) == 2:
                gear_ratio += adj_parts[0] * adj_parts[1]

    print("Gear ratio:", gear_ratio)
