# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 17:55:03 2020

@author: Be_Our_Guest
"""

def puzzle_input():
    with open("Input.txt", 'r') as file:
        lst = [i.strip().split(' ') for i in file.readlines()]

    for i in range(len(lst)):
        lst[i].append(0)
        lst[i].append(i)

    return lst

def execute_program(program, accumul, position):
    acu = accumul
    place = position
    #print(len(program))
    while program[place][2] == 0 and place < len(program):
        #print("Pos", place)
        if program[place][0] == 'nop':
            program[place][2] = 1
            if not place + 1 >= len(program):
                place += 1
                #print("Place", place)
            else:
                print("End of program hit! Value left in accumulator:", acu)
                return acu
        elif program[place][0] == 'acc':
            program[place][2] = 1
            if program[place][1][0] == '+':
                acu += int(program[place][1][1:])
                #print("Acc PLUS", place)
                if not place + 1 >= len(program):
                    place += 1
                else:
                    print("End of program hit! Value left in accumulator:", acu)
                    return acu
            elif program[place][1][0] == '-':
                acu -= int(program[place][1][1:])
                #print("Acc MINUS", place)
                if not place + 1 >= len(program):
                    place += 1
                else:
                    print("End of program hit! Value left in accumulator:", acu)
                    return acu
            else:
                print("CRASH! Acc has no + or -")
                break
        elif program[place][0] == 'jmp':
            program[place][2] = 1
            if program[place][1][0] == '+':
                if not place + int(program[place][1][1:]) >= len(program):
                    place += int(program[place][1][1:])
                else:
                    ("CRASH! Jumped to before start of data")
                    break
            elif program[place][1][0] == '-':
                if not place - int(program[place][1][1:]) < 0:
                    place -= int(program[place][1][1:])
                else:
                    print("CRASH! Jumped past end of data")
                    break
            else:
                print("CRASH! Jmp has no + or -")
                break
        else:
            print("CRASH! Command", program[place][0], "not valid")
        #print("Acc", accumulator)
    return acu

def main():
    '''
    The boot code is represented as a text file with one instruction per line of text.
    Each instruction consists of an operation (acc, jmp, or nop)
    and an argument (a signed number like +4 or -20).

    acc increases or decreases a single global value called the accumulator by the value given in the argument.
        For example, acc +7 would increase the accumulator by 7.
        The accumulator starts at 0.
        After an acc instruction, the instruction immediately below it is executed next.

    jmp jumps to a new instruction relative to itself.
        The next instruction to execute is found using the argument as an offset from the jmp
        instruction; for example, jmp +2 would skip the next instruction,
        jmp +1 would continue to the instruction immediately below it,
        and jmp -20 would cause the instruction 20 lines above to be executed next.

    nop stands for No OPeration - it does nothing.
        The instruction immediately below it is executed next.

    Immediately before any instruction is executed a second time, what value is in the accumulator?'''

    print("--------------- Part 1 ---------------\n")

    data = puzzle_input()

    #print(data)

    accumulator = execute_program(data, 0, 0)

    print("Value left in accumulator before infinite loop:", accumulator)

    print("\n--------------- Part 2 ---------------\n")

    '''After some careful analysis, you believe that exactly one instruction is corrupted.

    Somewhere in the program, either
        Case 1: A nop is supposed to be a jmp.
        Case 2: A jmp is supposed to be a nop

    The program is supposed to terminate by attempting to execute an instruction
    immediately after the last instruction in the file.

    By changing exactly one jmp or nop, you can repair the boot code and make it terminate correctly.

    Consider the previous example.

    Case 1:
        If you change the first instruction from nop +0 to jmp +0,
        it would create a single-instruction infinite loop, never leaving that instruction.

    Case 2:
        If you change almost any of the jmp instructions to a nop,
        the program will still eventually find another jmp instruction and loop forever.

        However, if you change the second-to-last instruction (from jmp -4 to nop -4),
        the program terminates!


    The instructions are visited in this order:
        nop +0  | 1
        acc +1  | 2
        jmp +4  | 3
        acc +3  |
        jmp -3  |
        acc -99 |
        acc +1  | 4
        nop -4  | 5
        acc +6  | 6

    After the last instruction (acc +6),
    the program terminates by attempting to run the instruction below the last instruction in the file.

    With this change, after the program terminates, the accumulator contains the value 8 (acc +1, acc +1, acc +6).

    Fix the program so that it terminates normally by changing exactly one jmp (to nop) or nop (to jmp).

    What is the value of the accumulator after the program terminates?'''

    data = puzzle_input()
    no_op = []
    jump = []

    for i in data:
        if i[0] == 'nop':
            no_op.append(i)
        elif i[0] == 'jmp':
            jump.append(i)

    #print("\nData", data)
    #print("\nNo op", no_op)
    #print("\nJump", jump)

    print("\nCase 1:")

    for i in no_op:
        #print(i)
        data = puzzle_input()
        #print("Data after case 1", data == puzzle_input())
        #print("nop", i)
        #print("Data before", data[i[3]])
        data[i[3]] = ['jmp', i[1], i[2], i[3]]
        #print("Data After", data[i[3]])
        accumulator = execute_program(data, 0, 0)


    data = puzzle_input()
    print("\nCase 2:")
    #print("Data after case 1", data == puzzle_input())


    for i in jump:
        i[2] = 1
        #print("Data after case 1", data == puzzle_input())
        data = puzzle_input()
        #print("jmp", i)
        #print("Data before", data[i[3]])
        data[i[3]] = ['nop', i[1], i[2], i[3]]
        #print("Data After", data[i[3]])
        accumulator = execute_program(data, 0, 0)



if __name__ == '__main__':
    main()