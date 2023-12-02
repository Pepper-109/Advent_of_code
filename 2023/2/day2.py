# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 12:51:07 2023

@author: Alix
"""

# ----------------------------- Part 1 -----------------------------

'''
To get information, once a bag has been loaded with cubes,
the Elf will reach into the bag,
grab a handful of random cubes, show them to you,
and then put them back in the bag.
He'll do this a few times per game.

Each game is listed with its ID number (like the 11 in Game 11: ...)
followed by a semicolon-separated list of subsets of cubes
that were revealed from the bag.

The Elf would first like to know which games would have been possible
if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes.

What is the sum of the IDs of those games?
'''

with open("input.txt", 'r') as file:
    valid_game_ID_sum = 0
    RED_LIMIT = 12
    GREEN_LIMIT = 13
    BLUE_LIMIT = 14

    for line in file.readlines():
        valid = True
        line = line.strip().split(": ")
        line[0] = int(line[0].split('Game ')[1])
        line[1] = line[1].split("; ")

        for pull in range(len(line[1])):
            line[1][pull] = line[1][pull].split(", ")

        # Simple pull-wise validation for now
        for pull in line[1]:
            for colour in pull:
                if "red" in colour:
                    if int(colour.split(" red")[0]) > RED_LIMIT:
                        valid = False
                        break
                if "green" in colour:
                    if int(colour.split(" green")[0]) > GREEN_LIMIT:
                        valid = False
                        break
                if "blue" in colour:
                    if int(colour.split(" blue")[0]) > BLUE_LIMIT:
                        valid = False
                        break

        if valid:
            valid_game_ID_sum += line[0]
            # print("VALID GAME:", line)

    print("Valid games:", valid_game_ID_sum)




# ----------------------------- Part 2 -----------------------------

'''
What is the fewest number of cubes of each colour
that could have been in the bag to make the game possible?
'''

with open("input.txt", 'r') as file:
    colour_power_sum = 0

    for line in file.readlines():
        red_min = 0
        green_min = 0
        blue_min = 0
        valid = True
        line = line.strip().split(": ")
        line[0] = int(line[0].split('Game ')[1])
        line[1] = line[1].split("; ")

        for pull in range(len(line[1])):
            line[1][pull] = line[1][pull].split(", ")

        # Track maximum value
        for pull in line[1]:
            for colour in pull:
                if "red" in colour:
                    if int(colour.split(" red")[0]) > red_min:
                        red_min = int(colour.split(" red")[0])
                if "green" in colour:
                    if int(colour.split(" green")[0]) > green_min:
                        green_min = int(colour.split(" green")[0])
                if "blue" in colour:
                    if int(colour.split(" blue")[0]) > blue_min:
                        blue_min = int(colour.split(" blue")[0])

        colour_power_sum += red_min*green_min*blue_min

    print("Colour power sum:", colour_power_sum)
