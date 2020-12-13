# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 00:02:04 2020

@author: Be_Our_Guest
"""

def puzzle_input():
    '''Formats puzzle input and stores in list'''
    with open('Input2.txt', 'r') as file:
        lst = [i.strip() for i in file]

    lyst = ''

    lust = []

    for i in lst:
        if len(i) != 0:
            lyst += ' ' + i
        else:
            lust.append(lyst)
            lyst = ''

    return lust

def check_valid_data(dat):
    '''Makes sure all required fields are present'''
    valid_data = []

    for i in dat:
        val = 1
        for j in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
            if j not in i:
                val = 0
        if val == 1:
            valid_data.append(i)
    return valid_data

def check_valid_data2(dat):
    ''' Formats data for part 2'''
    lst = []
    for i in enumerate(dat):
        i = i[0]
        lst.append(dat[i].split(' '))

    for i in enumerate(lst):
        i = i[0]
        for j in enumerate(lst[i]):
            j = j[0]
            lst[i][j] = lst[i][j].split(':')
    return lst

def byr(birth_year):
    ''' Checks if birth year is between 1920 and 2002 inclusive'''

    if not (int(birth_year) >= 1920 and int(birth_year) <= 2002):
        return False

    return True

def iyr(issue_year):
    ''' Checks if issue year is between 2010 and 2020 inclusive'''

    if not (int(issue_year) >= 2010 and int(issue_year) <= 2020):
        return False

    return True

def eyr(expiration_year):
    ''' Checks if expiration year is between 2020 and 2030 inclusive'''

    if not (int(expiration_year) >= 2020 and int(expiration_year) <= 2030):
        return False

    return True

def height_check(height):
    ''' Ensures height is in cm or in, and height is in a valid range'''

    if height[-2:] not in ['cm', 'in']:
        return False

    if height[-2:] == 'cm':
        #print(height[:-2])
        if not (int(height[:-2]) >= 150 and int(height[:-2]) <= 193):
            #print("remove", height[:-2])
            return False

    if height[-2:] == 'in':
        if not (int(height[:-2]) >= 59 and int(height[:-2]) <= 76):
            return False

    return True

def hair_colour(hair_col, num, let):
    ''' Ensures the first character is #, length of field is 6, and valid character set'''
    if hair_col[0] != '#':
        return False

    if len(hair_col[1:]) != 6:
        return False

    for i in hair_col[1:]:
        if not (i in num or i in let):
            return False

    return True

def passport_id(passport, num):
    ''' Ensures password has a length of 9 and has a valid character set'''
    if len(passport) != 9:
        return False

    for i in passport[1:]:
        if i not in num:
            return False

    return True

def remove_invalid(to_remove, dat):
    ''' Removes invalid passports in part 2 from valid passport list'''
    for i in to_remove:
        if i in dat:
            dat.remove(i)
    return dat

def main():
    '''
    Expected fields:
        byr (Birth Year)
        iyr (Issue Year)
        eyr (Expiration Year)
        hgt (Height)
        hcl (Hair Color)
        ecl (Eye Color)
        pid (Passport ID)
        cid (Country ID) - OPTIONAL

    Part 2:

        byr (Birth Year) - four digits; at least 1920 and at most 2002.
        iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        hgt (Height) - a number followed by either cm or in:
            If cm, the number must be at least 150 and at most 193.
            If in, the number must be at least 59 and at most 76.
        hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        pid (Passport ID) - a nine-digit number, including leading zeroes.

        cid (Country ID) - ignored, missing or not.
        '''

    data = puzzle_input()

    #print(data)

    print("\n------------------- Part 1 --------------------\n")

    valid_data = check_valid_data(data)

    print("Number of valid passports:", len(valid_data))

    print("\n------------------- Part 2 --------------------\n")

    valid_data2 = check_valid_data2(valid_data)

    #print(valid_data2)

    to_be_removed = []

    numbers = ['0','1','2','3','4','5','6','7','8','9']
    letters = ['a','b','c','d','e','f']
    eye_colours = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    for i in valid_data2:
        for j in i:
            if j[0] == 'byr': # At least 1920 and at most 2002
                if not byr(j[1]):
                    to_be_removed.append(i)

            elif j[0] == 'iyr': # At least 2010 and at most 2020
                #print(j)
                if not iyr(j[1]):
                    to_be_removed.append(i)

            elif j[0] == 'eyr': # At least 2020 and at most 2030
                #print(j)
                if not eyr(j[1]):
                    to_be_removed.append(i)

            elif j[0] == 'hgt': # a number followed by either cm or in
                                #cm, at least 150 and at most 193
                                #in, the number must be at least 59 and at most 76
                #print(j[1][-2:])
                if not height_check(j[1]):
                    to_be_removed.append(i)

            elif j[0] == 'hcl': # a # followed by exactly six characters 0-9 or a-f
                if not hair_colour(j[1], numbers, letters):
                    to_be_removed.append(i)

            elif j[0] == 'ecl': #  exactly one of: amb blu brn gry grn hzl oth
                #print(j)
                if j[1] not in eye_colours:
                    to_be_removed.append(i)

            elif j[0] == 'pid': # a nine-digit number, including leading zeroes
                #print(j)
                if not passport_id(j[1], numbers):
                    to_be_removed.append(i)

    valid_data2 = remove_invalid(to_be_removed, valid_data2)

    #print(valid_data2)
    print("Number of valid passports with additional requirements:", len(valid_data2))


if __name__ == '__main__':
    main()
