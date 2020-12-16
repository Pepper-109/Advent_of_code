# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 12:51:53 2020

@author: Be_Our_Guest
"""

def puzzle_input():
    with open('test-Input.txt', 'r') as file:
        lst = [i.strip().split(' ') for i in file.readlines()]

    group = []
    groups = []

    #print(lst)

    for i in lst:
        if i[0] != 'mask':
            group.append(i)
        else:
            groups.append(group)
            group = []

    return groups

def main():

    '''
        The initialization program (your puzzle input) can
        either update the bitmask or write a value to memory.

        Values and memory addresses are both 36-bit unsigned integers.

        For example, ignoring bitmasks for a moment,
        a line like mem[8] = 11 would write the value 11 to memory address 8.


    '''

    data = puzzle_input()

    print(data)




if __name__ == '__main__':
    main()