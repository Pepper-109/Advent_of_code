# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 10:50:42 2020

@author: Be_Our_Guest
"""

def puzzle_input():
    '''Formats puzzle input and stores in list, returns said list'''
    with open("test-Input2.txt", 'r') as file:
        lst = [i.strip() for i in file.readlines()]


    for row in range(len(lst)):
        r = []
        for seat in lst[row]:
            r.append(seat)
        lst[row] = r

    return lst

def visualize(dat):
    print()
    for i in dat:
        for j in i:
            print(j, end=(''))
        print()
    return

def seat_count(seats):
    neighbours = []
    for row in range(len(seats)):
        for seat in range(len(seats[row])):
            occupied = 0
            if seat == 0:
                if row == 0:
                    for i in [seats[row][seat+1], seats[row+1][seat+1], seats[row+1][seat]]:
                        #print(i)
                        if i == '#':
                            occupied += 1
                    #print(seats[row][seat], [seats[row][seat+1], seats[row+1][seat]])
                elif row == len(seats) - 1:
                    for i in [seats[row-1][seat], seats[row-1][seat+1], seats[row][seat+1]]:
                        if i == '#':
                            occupied += 1
                    #print(seats[row][seat], [seats[row-1][seat], seats[row][seat+1]])
                else:
                    for i in [seats[row-1][seat], seats[row-1][seat+1], seats[row][seat+1], seats[row+1][seat+1], seats[row+1][seat]]:
                        if i == '#':
                            occupied += 1
                    #print(seats[row][seat], [seats[row-1][seat], seats[row][seat+1], seats[row+1][seat]])
            elif seat == len(seats[row]) - 1:
                if row == 0:
                    for i in [seats[row][seat-1], seats[row+1][seat-1], seats[row+1][seat]]:
                        if i == '#':
                            occupied += 1
                    #print(seats[row][seat], [seats[row][seat-1], seats[row+1][seat]])
                elif row == len(seats) - 1:
                    for i in [seats[row-1][seat], seats[row-1][seat-1], seats[row][seat-1]]:
                        if i == '#':
                            occupied += 1
                    #print(seats[row][seat], [seats[row-1][seat], seats[row][seat-1]])
                else:
                    for i in [seats[row-1][seat], seats[row-1][seat-1], seats[row][seat-1], seats[row+1][seat-1], seats[row+1][seat]]:
                        if i == '#':
                            occupied += 1
                    #print(seats[row][seat], [seats[row-1][seat], seats[row][seat-1], seats[row+1][seat]])
            elif row == 0:
                for i in [seats[row][seat-1], seats[row+1][seat-1], seats[row+1][seat], seats[row+1][seat+1], seats[row][seat+1]]:
                        if i == '#':
                            occupied += 1
                #print(seats[row][seat], [seats[row][seat-1], seats[row+1][seat], seats[row][seat+1]])
            elif row == len(seats) - 1:
                for i in [seats[row][seat-1], seats[row-1][seat-1], seats[row-1][seat], seats[row-1][seat+1], seats[row][seat+1]]:
                        if i == '#':
                            occupied += 1
                #print(seats[row][seat], [seats[row][seat-1], seats[row-1][seat], seats[row][seat+1]])
            else:
                for i in [seats[row][seat-1], seats[row-1][seat-1], seats[row-1][seat], seats[row-1][seat+1], seats[row][seat+1], seats[row+1][seat+1], seats[row+1][seat], seats[row+1][seat-1]]:
                        if i == '#':
                            occupied += 1
                #if row == 5 and seat == 4:
                #   print(seats[row][seat], occupied, [seats[row][seat-1], seats[row-1][seat-1], seats[row-1][seat], seats[row-1][seat+1], seats[row][seat+1], seats[row+1][seat+1], seats[row+1][seat], seats[row+1][seat-1]])
                #print(seats[row][seat], [seats[row][seat-1], seats[row-1][seat], seats[row][seat+1], seats[row+1][seat]])

            neighbours.append([row, seat, occupied])

    return neighbours

def next_generation(seat_info, gen, tolerance):
    for i in seat_info:
        #print(i)
        #print(gen[i[0]][i[1]])
        if gen[i[0]][i[1]] == 'L':
            if i[2] == 0:
                gen[i[0]][i[1]] = '#'
        elif gen[i[0]][i[1]] == '#':
            if i[2] >= tolerance:
                gen[i[0]][i[1]] = 'L'
        elif gen[i[0]][i[1]] != '.':
            print("Invalid seat type:", gen[i[0]][i[1]])

    return gen

def seat_count_part_2(seats):
    neighbours = []
    for row in range(len(seats)):
        for seat in range(len(seats[row])):
            occupied = 0
            if seat == 0:
                if row == 0:
                    for i in [seats[row][seat+1], seats[row+1][seat+1], seats[row+1][seat]]:
                        #print(i)
                        if i == '#':
                            occupied += 1
                    #print(seats[row][seat], [seats[row][seat+1], seats[row+1][seat]])
                elif row == len(seats) - 1:
                    for i in [seats[row-1][seat], seats[row-1][seat+1], seats[row][seat+1]]:
                        if i == '#':
                            occupied += 1
                    #print(seats[row][seat], [seats[row-1][seat], seats[row][seat+1]])
                else:
                    for i in [seats[row-1][seat], seats[row-1][seat+1], seats[row][seat+1], seats[row+1][seat+1], seats[row+1][seat]]:
                        if i == '#':
                            occupied += 1
                    #print(seats[row][seat], [seats[row-1][seat], seats[row][seat+1], seats[row+1][seat]])
            elif seat == len(seats[row]) - 1:
                if row == 0:
                    for i in [seats[row][seat-1], seats[row+1][seat-1], seats[row+1][seat]]:
                        if i == '#':
                            occupied += 1
                    #print(seats[row][seat], [seats[row][seat-1], seats[row+1][seat]])
                elif row == len(seats) - 1:
                    for i in [seats[row-1][seat], seats[row-1][seat-1], seats[row][seat-1]]:
                        if i == '#':
                            occupied += 1
                    #print(seats[row][seat], [seats[row-1][seat], seats[row][seat-1]])
                else:
                    for i in [seats[row-1][seat], seats[row-1][seat-1], seats[row][seat-1], seats[row+1][seat-1], seats[row+1][seat]]:
                        if i == '#':
                            occupied += 1
                    #print(seats[row][seat], [seats[row-1][seat], seats[row][seat-1], seats[row+1][seat]])
            elif row == 0:
                for i in [seats[row][seat-1], seats[row+1][seat-1], seats[row+1][seat], seats[row+1][seat+1], seats[row][seat+1]]:
                        if i == '#':
                            occupied += 1
                #print(seats[row][seat], [seats[row][seat-1], seats[row+1][seat], seats[row][seat+1]])
            elif row == len(seats) - 1:
                for i in [seats[row][seat-1], seats[row-1][seat-1], seats[row-1][seat], seats[row-1][seat+1], seats[row][seat+1]]:
                        if i == '#':
                            occupied += 1
                #print(seats[row][seat], [seats[row][seat-1], seats[row-1][seat], seats[row][seat+1]])
            else:
                for i in [seats[row][seat-1], seats[row-1][seat-1], seats[row-1][seat], seats[row-1][seat+1], seats[row][seat+1], seats[row+1][seat+1], seats[row+1][seat], seats[row+1][seat-1]]:
                        if i == '#':
                            occupied += 1
                #if row == 5 and seat == 4:
                #   print(seats[row][seat], occupied, [seats[row][seat-1], seats[row-1][seat-1], seats[row-1][seat], seats[row-1][seat+1], seats[row][seat+1], seats[row+1][seat+1], seats[row+1][seat], seats[row+1][seat-1]])
                #print(seats[row][seat], [seats[row][seat-1], seats[row-1][seat], seats[row][seat+1], seats[row+1][seat]])

            neighbours.append([row, seat, occupied])

    return neighbours



def main():
    '''

    Each position is either floor (.), an empty seat (L), or an occupied seat (#).

    All decisions are based on the number of occupied seats adjacent to a given seat
    (one of the eight positions immediately up, down, left, right, or diagonal
     from the seat).

    The following rules are applied to every seat simultaneously:

    If a seat is empty (L) and there are no occupied seats adjacent to it,
    the seat becomes occupied.

    If a seat is occupied (#) and four or more seats adjacent to it
    are also occupied, the seat becomes empty.

    Otherwise, the seat's state does not change.

    Floor (.) never changes; seats don't move, and nobody sits on the floor.

    Test input:
        Once people stop moving around, you count 37 occupied seats.

    Simulate your seating area by applying the seating rules repeatedly
    until no seats change state. How many seats end up occupied?

    --- Part Two ---
    As soon as people start to arrive, you realize your mistake.
    People don't just care about adjacent seats -
    they care about the first seat they can see in each of those eight directions!

    Now, instead of considering just the eight immediately adjacent seats,
    consider the first seat in each of those eight directions.

    For example, the empty seat below would see eight occupied seats: (test-Input2)

                                    .......#.
                                    ...#.....
                                    .#.......
                                    .........
                                    ..#L....#
                                    ....#....
                                    .........
                                    #........
                                    ...#.....

    test-Input3: 0 occ seats
    test-Input4: 0 occ seats
    '''

    data = puzzle_input()

    #print(data)

    visualize(data)

    #print(data[0][0])

    occ = seat_count(data)

    #print(occ)
    new_occ_count = 0
    curr_occ_count = 1

    current_gen = data

    while new_occ_count != curr_occ_count:
        new_occ_count = 0
        curr_occ_count = 0

        for i in current_gen:
            for j in i:
                if j == '#':
                    curr_occ_count += 1

        occ = seat_count(current_gen)

        current_gen = next_generation(occ, current_gen, 4)

        #visualize(current_gen)

        for i in current_gen:
            for j in i:
                if j == '#':
                    new_occ_count += 1


    print("\nThe number of occupied seats is", new_occ_count)


    print("\n-------------- Part 2 ---------------\n")



if __name__ == '__main__':
    main()