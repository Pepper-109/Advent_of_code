# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 23:59:50 2020

@author: Be_Our_Guest
"""

def puzzle_input():
    '''Formats puzzle input and stores in list'''
    with open('Input.txt', 'r') as file:
        lst = [i.strip().split(' ') for i in file.readlines()]

    group = []
    groups = []

    for i in lst:
        if i[0] != '':
            group.append(i)
        else:
            groups.append(group)
            group = []

    return groups

def unique_answers_per_group(dat):
    '''Returns a list of unique answers by group'''
    uni = []
    for i in dat:
        uniq = []

        for person in i:

            for answer in person:

                for letter in answer:
                    #print("L", l)
                    uniq.append(letter)

        #print(uniq)
        uni.append(set(uniq))

    return uni

def main():
    '''The form asks a series of 26 yes-or-no questions marked a through z.
    All you need to do is identify the questions for which anyone in your group answers "yes".

    For each of the people in their group, you write down the questions for which they answer "yes",
    one per line. For example:

    abcx
    abcy
    abcz

    In this group, there are 6 questions to which anyone answered "yes": a, b, c, x, y, and z.
    (Duplicate answers to the same question don't count again)'''

    data = puzzle_input()

    #print(data)

    unique = unique_answers_per_group(data)

    #print(unique)

    yes_count = 0

    for i in unique:
        yes_count += len(i)

    print("Number of questions answered \"yes\":", yes_count)

    print("\n------------------ Part 2 --------------------\n")

    # How many questions did everyone answer "yes" to in their group?

    group_yes = 0

    for i in enumerate(data):
        i = i[0]
        #print("data", data[i], len(data[i]))

        if len(data[i]) == 1:
            group_yes += len(data[i][0][0])

        else:
            lst = []

            for j in data[i]:

                for k in j[0]:
                    #print("k", k)
                    lst.append(k)

            #print(lst)
            lst = set(lst)
            #print(lst)
            to_be_removed = []

            for letter in lst:
                #print(letter)

                for answer in data[i]:
                    #print(answer)

                    if letter not in answer[0]:
                        #print("remove", m)
                        to_be_removed.append(letter)

            to_be_removed = set(to_be_removed)

            for to_remove in to_be_removed:
                lst.remove(to_remove)

            #print(lst)
            group_yes += len(lst)

    print("Number of questions answered \"yes\" by everyone:",group_yes)

if __name__ == '__main__':
    main()
