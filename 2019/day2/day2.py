# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 13:23:15 2020

@author: Be_Our_Guest
"""

'''
Opcode 1 adds together numbers read from the next two positions and stores the result in a third position.

Opcode 2 works exactly like opcode 1, except it multiplies the two inputs instead of adding them.

99 means that the program is finished and should immediately halt. 

Encountering an unknown opcode means something went wrong.
'''

def runIntCode(lst):
    for i in range(len(lst)):
        if i % 4 == 0:
            if lst[i] == 1:
                lst[lst[i+3]] = lst[lst[i+1]] + lst[lst[i+2]]
            elif lst[i] == 2:
                lst[lst[i+3]] = lst[lst[i+1]] * lst[lst[i+2]]
            elif lst[i] == 99:
                #print("Ending program")
                break;
            else:
                print("CRASH!!!")
    return lst

def main():
    data = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,9,1,19,1,19,5,23,1,23,6,27,2,9,27,31,1,5,31,35,1,35,10,39,1,39,10,43,2,43,9,47,1,6,47,51,2,51,6,55,1,5,55,59,2,59,10,63,1,9,63,67,1,9,67,71,2,71,6,75,1,5,75,79,1,5,79,83,1,9,83,87,2,87,10,91,2,10,91,95,1,95,9,99,2,99,9,103,2,10,103,107,2,9,107,111,1,111,5,115,1,115,2,119,1,119,6,0,99,2,0,14,0]
    
    data[1] = 12
    data[2] = 2
    
    dataP1 = runIntCode(data)
    
    print(dataP1[0])
    
    print(data)
    
    print("\n------------------- Part 2 --------------------\n")
    
    for j in range(0,100):
        for k in range(0, 100):
            dataP2 = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,9,1,19,1,19,5,23,1,23,6,27,2,9,27,31,1,5,31,35,1,35,10,39,1,39,10,43,2,43,9,47,1,6,47,51,2,51,6,55,1,5,55,59,2,59,10,63,1,9,63,67,1,9,67,71,2,71,6,75,1,5,75,79,1,5,79,83,1,9,83,87,2,87,10,91,2,10,91,95,1,95,9,99,2,99,9,103,2,10,103,107,2,9,107,111,1,111,5,115,1,115,2,119,1,119,6,0,99,2,0,14,0]
            dataP2[1] = j
            dataP2[2] = k
            
            dataP2 = runIntCode(dataP2)

            if dataP2[0] == 19690720:
                print(j, k)
                print(j*k)
    
if __name__ == '__main__':
    main()