# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 09:29:52 2020

@author: Be_Our_Guest
"""

def puzzle_input():
    '''Formats puzzle input and stores in list'''
    with open('Input.txt', 'r') as file:
        lst = [i.strip().split(' ') for i in file.readlines()]
        for i in lst:
            i[0] = i[0].split('-')
            i[0][0] = int(i[0][0])
            i[0][1] = int(i[0][1])
            i[1] = i[1].replace(':', '')
    return lst

def main():
    '''
    Part 1:

    1-3 a: abcde
    1-3 b: cdefg
    2-9 c: ccccccccc
    Each line gives the password policy and then the password.
    The policy indicates the lowest/highest number of times a given letter must appear to be valid.
    For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

    Part 2:

    The policy describes two positions in the password, where 1 means the first character,
    2 means the second character, and so on.
    (Be careful; Toboggan Corporate Policies have no concept of "index zero"!)
    Exactly one of these positions must contain the given letter.
    Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

    Given the same example list from above:

    1-3 a: abcde is valid: position 1 contains a and position 3 does not.
    1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
    2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
    '''

    data = puzzle_input()

    valid_passwords = []

    for i in data:
        lower = i[0][0]
        upper = i[0][1]
        letter = i[1]
        if lower <= i[2].count(letter) and upper >= i[2].count(letter):
            valid_passwords.append(i)

    print("The number of valid passwords using the old policy is:", len(valid_passwords))

    print("\n----------------------- Part 2 ------------------------\n")

    new_policy = []

    for i in data:
        pos1 = i[0][0] - 1
        pos2 = i[0][1] - 1
        letter = i[1]
        if (i[2][pos1] == letter) ^ (i[2][pos2] == letter): #Bitwise XOR: ^
            new_policy.append(i)

    print("The number of valid passwords using the new policy is:", len(new_policy))

if __name__ == '__main__':
    main()
