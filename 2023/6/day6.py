# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 12:16:37 2023

@author: Alix
"""

# ----------------------------- Part 1 -----------------------------

print("----------------------------- Part 1 -----------------------------")

'''
The time allowed for each race and also the WR for that race.

Go farther in each race than the current record holder.

Each boat has a big button on top.

Holding down the button charges the boat, releasing allows the boat to move.

Time spent holding the button counts against the total race time.

You can only hold the button at the start of the race.

Boats don't move until the button is released.

Your toy boat has a starting speed of zero millimeters per millisecond.

For each whole millisecond you spend holding down the button,
the boat's speed increases by one millimeter per millisecond.

Determine the number of ways you could beat the record in each race.
What do you get if you multiply these numbers together?
'''

with open("input.txt", 'r') as file:
    for line in file.readlines():
        line = line.strip()

        if "Time" in line:
            times = [int(x) for x in line.split(":\t")[1].split("\t")]
        else:
            distances = [int(x) for x in line.split(":\t")[1].split("\t")]

margin_of_error = 1

for time, distance in zip(times, distances):
    valid_holds = 0

    for hold_button_for in range(0, time + 1):
        dist = hold_button_for * (time - hold_button_for)

        if dist > distance:
            valid_holds += 1

    margin_of_error *= valid_holds

print("The margin for error is:", margin_of_error)

# ----------------------------- Part 2 -----------------------------

print("----------------------------- Part 2 -----------------------------")

'''
You realize the piece of paper actually just has very bad kerning.

There's really only one race, ignore the spaces between the numbers on each line.
'''

with open("input.txt", 'r') as file:
    for line in file.readlines():
        line = line.strip()

        if "Time" in line:
            time = ''

            for x in line.split(":\t")[1].split("\t"):
                time = time + x

            time = int(time)
        else:
            distance = ''

            for x in line.split(":\t")[1].split("\t"):
                distance = distance + x

            distance = int(distance)

valid_holds = 0

for hold_button_for in range(0, time + 1):
    dist = hold_button_for * (time - hold_button_for)

    if dist > distance:
        valid_holds += 1

print("The margin for error is:", valid_holds)
