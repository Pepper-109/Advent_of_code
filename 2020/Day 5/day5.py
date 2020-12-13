# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 11:13:30 2020

@author: Be_Our_Guest
"""

def puzzle_input():
    '''Formats puzzle input and stores in list'''
    with open('Input.txt', 'r') as file:
        lst = [i.strip() for i in file.readlines()]
    return lst

def lower(low, high):
    ''' Calculates and returns lower bound'''
    return ((high - low) // 2) + 1 + low

def upper(low, high):
    ''' Calculates and returns upper bound'''
    return (low + high) // 2

def main():
    '''
    FBFBBFFRLR

    Start by considering the whole range, rows 0 through 127.
    F means to take the lower half, keeping rows 0 through 63.
    B means to take the upper half, keeping rows 32 through 63.
    F means to take the lower half, keeping rows 32 through 47.
    B means to take the upper half, keeping rows 40 through 47.
    B keeps rows 44 through 47.
    F keeps rows 44 through 45.
    The final F keeps the lower of the two, row 44.
    '''

    data = puzzle_input()

    #print(data)

    passes = []

    for i in data:
        row = 0
        column = 0
        seat_id = 0
        lower_row = 0
        upper_row = 127
        lower_column = 0
        upper_column = 7
        for j in i[0:7]:
            #print(j)
            if j == 'F':
                upper_row = upper(lower_row, upper_row)
            if j == 'B':
                lower_row = lower(lower_row, upper_row)
            #print(lower_row, upper_row)
        row = upper_row
        for j in i[7:]:
            #print(j)
            if j == 'L':
                upper_column = upper(lower_column, upper_column)
            if j == 'R':
                lower_column = lower(lower_column, upper_column)
            #print(lower_column, upper_column)
        column = upper_column
        seat_id = (row * 8) + column
        passes.append({"Row": row, "Column": column, "seat_id": seat_id})

    passes = sorted(passes, key=lambda x: x['seat_id'], reverse=True)

    print("Highest seat ID is", passes[0]['seat_id'])

    print("\n------------- Part 2 -------------\n")

    #The seats with IDs +1 and -1 from yours will be in your list.

    for i in range(len(passes) - 1):
        if (passes[i]['seat_id'] + passes[i+1]['seat_id']) % 2 == 0:
            print("My seat ID is", (passes[i]['seat_id'] + passes[i+1]['seat_id']) // 2)
            break


if __name__ == '__main__':
    main()
