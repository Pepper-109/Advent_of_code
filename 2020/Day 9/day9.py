# -*- coding: utf-8 -*-
"""
Created on Tue Dec  9 17:55:03 2020

@author: Be_Our_Guest
"""

def puzzle_input():
    '''Formats puzzle input and stores in list, returns said list'''
    with open("Input.txt", 'r') as file:
        lst = [int(i.strip()) for i in file.readlines()]

    return lst

def check_valid(dat, preamble, sum_of):
    ''' Used in part 1 to find the first number that fails the check'''
    for position in enumerate(dat):
        if position[0] > preamble:
            valid = 0
            add_range = dat[position[0]-preamble-1:position[0]-1]
            #print(add_range)
            for i in enumerate(add_range):
                for j in enumerate(add_range):
                    #print(to_sum[i:j])
                    #print(sum(to_sum[i:j]))
                    #print(invalid_num[2])
                    if i[1] + j[1] == dat[position[0]-1]:
                        valid = 1
                    #print(comb)
            if valid == 0:
                return [sum_of, preamble, dat[position[0]-1], position[0]-1]
    return ["Nothing out of order here", 0, 0]

def encryp_weak(to_sum, invalid_num):
    ''' Creates every combination of length n and returns the smallest sum
        of the lowest and highest value in the combinations'''
    mini = []
    #print(len(to_sum))
    #print(to_sum[0])
    #print(min_pos)

    for i in enumerate(to_sum):
        for j in enumerate(to_sum):
            #print(to_sum[i:j])
            #print(sum(to_sum[i:j]))
            #print(invalid_num[2])
            if sum(to_sum[i[0]:j[0]]) == invalid_num[2]:
                minim = to_sum[i[0]:j[0]]
                minim.sort()
                #print(minim)
                mini.append(minim[0] + minim[-1])

    return mini

def main():
    '''
        What is the first number to not be the sum of a combination of the
        last preamble length numbers.

        ------------------------- Part 2 -------------------

        The final step in breaking the XMAS encryption relies on the invalid number you just found:
        you must find a contiguous set of at least two numbers in your list which sum to
        the invalid number from step 1.

        In the example list, adding up all of the numbers from 15 through 40 produces
        the invalid number from step 1, 127.

        (Of course, the contiguous set of numbers in your actual list might be much longer.)

        To find the encryption weakness,
        add together the smallest and largest number in this contiguous range;
        in this example, these are 15 and 47, producing 62.'''

    data = puzzle_input()

    #print(data)

    first_to_f = check_valid(data, 25, 2)

    print("\nThe first number to not be a sum of", first_to_f[0],
          "the last", first_to_f[1], "numbers is", first_to_f[2],
          "at position", first_to_f[3])

    #print(data[first_to_f[3]])

    print("\n----------------- Part 2 -----------------\n")


    encryption_weakness = encryp_weak(data, first_to_f)

    print("The encryption weakness is", min(encryption_weakness))



if __name__ == '__main__':
    main()
