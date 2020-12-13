# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 23:58:05 2020

@author: Be_Our_Guest
"""

def puzzle_input():
    '''


    Returns
    -------
    lst : list
        Formatted puzzle input.

    '''

    with open('input.txt', 'r') as file:
        lst = [int(i.strip()) for i in file.readlines()]
    return lst

def find_pair(lst):
    '''


    Parameters
    ----------
    lst : list
        Puzzle input.

    Returns
    -------
    pear : list
         List with indices i, j such that i + j = 2020.

    '''
    pear = []
    for i in lst:
        for j in lst:
            if (i + j) == 2020:
                pear.append(i)
                pear.append(j)
    return pear

def find_triplet(lst):
    '''


    Parameters
    ----------
    lst : list
        Puzzle input.

    Returns
    -------
    trip : list
        List with indices i, j, k such that i + j + k = 2020.

    '''
    trip = []
    for i in lst:
        for j in lst:
            for k in lst:
                if (i + j + k) == 2020:
                    trip.append(i)
                    trip.append(j)
                    trip.append(k)
    return trip

def main():
    '''
     Find 2 entries that sum to 2020, answer is the multiple of them.

    '''

    data = puzzle_input()

    print(data)

    pair = find_pair(data)

    print(pair[0]*pair[1])

    print("\n--------------- Part 2 -----------------\n")

    triplet = find_triplet(data)

    print(triplet[0]*triplet[1]*triplet[2])


if __name__ == '__main__':
    main()
