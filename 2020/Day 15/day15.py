# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 13:24:05 2020

@author: Be_Our_Guest
"""
from time import perf_counter
start = perf_counter()
def puzzle_input():
    '''Formats puzzle input and stores in list'''
    with open('test-Input1.txt', 'r') as file:
        lst = [i.strip().split(',') for i in file.readlines()]

    for i in range(len(lst[0])):
        lst.append(int(lst[0][i]))

    lst.pop(0)

    return lst

def main():
    '''
    If that was the first time the number has been spoken, the current player says 0.
    Otherwise the current player announces how many turns apart
    the number is from when it was previously spoken.

    Since it had been spoken before, the next number to speak is
    the difference between the turn number when it was last spoken
    (the previous turn, 4) and the turn number of the time it was most
    recently spoken before then (turn 1).
    Thus, the 5th number spoken is 4 - 1, 3.

    First test input should be 0,3,6,0,3,3,1,0,4,0
    '''

    data = puzzle_input()

    new = set(data[:-1])

    data.reverse()

    print(data)

    print(new)

    while len(data) < 2020:
        if data[0] not in new:
            new.add(data[0])
            data.insert(0, 0)
            #print(len(new))
        else:
            if len(data) % 100000 == 0:
                print(perf_counter() - start)
            #print(data)
            pos = data.index(data[0], 1)
            '''pos = 1
            while True:
                if data[pos] == data[0]:
                    #print(data)
                    break
                pos += 1'''
            data.insert(0, pos)

    #print(data)

    print(data[0])


    '''data = puzzle_input()

    print(data)

    while len(data) < 30000000:
        if data.count(data[-1]) == 1:
            data.append(0)
        elif data.count(data[-1]) > 1:
            #print(data)
            #data.reverse()
            pos = len(data) - 2
            if pos % 1000 == 0:
                print(pos)
            while True:
                #print(pos)
                if data[pos] == data[-1]:
                    break
                pos -= 1
            data.append(len(data) - pos - 1)

    #print(data)

    print(data[-1])'''


if __name__ == '__main__':
    main()