# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 00:24:40 2023

@author: Alix
"""

# ----------------------------- Part 1 -----------------------------
'''
On each line, combine the first digit and the last digit to form a
single two-digit number.

What is the sum of all of the calibration values?
'''

with open("input.txt", 'r') as file:
    calibration_sum = 0

    for line in file.readlines():
        line = line.strip()
        numbers = []

        for i in range(0, 10):
            if str(i) in line:
                numbers.append([i, line.index(str(i))])
                numbers.append([i, line.rindex(str(i))])

        sorted_num = list(sorted(numbers, key=lambda item: item[1]))

        calibration_sum += int(str(sorted_num[0][0]) + str(sorted_num[-1][0]))

print("The sum of all of the calibration values is:", calibration_sum)


# ----------------------------- Part 2 -----------------------------
'''
It looks like some of the digits are actually spelled out with letters:
one, two, three, four, five, six, seven, eight, and nine
also count as valid "digits".
'''

with open("input.txt", 'r') as file:
    calibration_sum = 0
    written_numbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
                "six": 6, "seven": 7, "eight": 8, "nine": 9}

    for line in file.readlines():
        line = line.strip()
        numbers = []

        for i in range(0, 10):
            if str(i) in line:
                numbers.append([i, line.index(str(i))])
                numbers.append([i, line.rindex(str(i))])

        for num, value in written_numbers.items():
            if num in line:
                numbers.append([value, line.index(num)])
                numbers.append([value, line.rindex(num)])

        sorted_num = list(sorted(numbers, key=lambda item: item[1]))

        calibration_sum += int(str(sorted_num[0][0]) + str(sorted_num[-1][0]))

print("The sum of all of the calibration values is:", calibration_sum)
