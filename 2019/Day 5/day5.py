# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 13:52:22 2020

@author: Be_Our_Guest
"""
def opCode3(lst, address, inp):
    lst[address] = inp

def opCode4(lst, param):
    return lst[param]

def runIntCode(lst):
    inp = 0
    i = 0
    
    while i < len(lst):
        opCode = int(str(lst[i])[-2])*10 + int(str(lst[i])[-1])
        print(opCode)
        param = [int(str(lst[i])[1]), int(str(lst[i])[0]), int(str(lst[i])[2])]
        print(param)
        if opCode == 1:
            if param[0] == 0:
                param1 = lst[lst[i+1]]
            else:
                param1 = lst[i+1]
            if param[1] == 0:
                param2 = lst[lst[i+2]]
            else:
                param2 = lst[i+2]
            if param[2] == 0:
                param3 = lst[lst[i+3]]
            else:
                param3 = lst[i+3]
            lst[param3] = param1+param2
            i += 4
        elif opCode == 2:
            if param[0] == 0:
                param1 = lst[lst[i+1]]
            else:
                param1 = lst[i+1]
            if param[1] == 0:
                param2 = lst[lst[i+2]]
            else:
                param2 = lst[i+2]
            if param[2] == 0:
                param3 = lst[lst[i+3]]
            else:
                param3 = lst[i+3]
            lst[param3] = param1*param2
            i += 4
        elif opCode == 3:
            opCode3(lst, lst[lst[i+1]], inp)
            i += 3
        elif opCode == 4:
            opCode4(lst, param)
            i += 3
        elif opCode == 99:
            return lst
        else:
            print("CRASH!!!")
            return lst
    return lst

def main():
    '''
    Opcode 3 takes a single integer as input and saves it to the position given by its only parameter. 
    For example, the instruction 3,50 would take an input value and store it at address 50.
    
    Opcode 4 outputs the value of its only parameter. 
    For example, the instruction 4,50 would output the value at address 50.'''
    
    data = [1002,4,3,4,33]
    
    dataP1 = runIntCode(data)

if __name__ == '__main__':
    main()