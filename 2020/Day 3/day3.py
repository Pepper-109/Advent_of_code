# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 00:03:38 2020

@author: Be_Our_Guest
"""

def puzzle_input():
    '''Formats puzzle input and stores in list'''
    with open('Input.txt', 'r') as file:
        lst = [i.strip().split('\n') for i in file.readlines()]
    return lst

def tree_count(data, directions):
    '''Counts the number of trees intercepted and returns as list'''
    tree = []

    for j in directions:
        pos = [0,0]
        tree_hit_count = 0
        for _ in range((len(data) // j[1]) -1):
            # Right
            pos[0] = (pos[0] + j[0]) % len(data[0][0])
            # Down
            pos[1] += j[1]
            # Check if tree
            if data[pos[1]][0][pos[0]] == '#':
                tree_hit_count += 1
        tree.append([j, tree_hit_count])
    return tree

def mult_tree(tree_list):
    '''Multiplies the number of trees hit together'''
    multi_tree = 1
    for tree in tree_list:
        multi_tree *= tree[1]
    return multi_tree

def main():
    '''
    Count the number of trees you encounter by going 3 right, 1 down.
    Tree pattern repeats to the right forever.

    Part 2:

    Determine the number of trees you would encounter for each of the following slopes:

    Right 1, down 1.
    Right 3, down 1. (This is the slope you already checked.)
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.

    In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively;
    Multiplied together, these produce the answer 336.

    '''

    data = puzzle_input()

    trees = tree_count(data, [[3,1]])

    multiple_trees = mult_tree(trees)

    print(trees)

    print(multiple_trees)

    print("\n---------------------- Part 2---------------------\n")

    #R1, down 1. Right 3, down 1. Right 5, down 1. Right 7, down 1. Right 1, down 2.
    trees2 = tree_count(data, [[3, 1], [1, 1], [5, 1], [7, 1], [1, 2]])

    multiple_trees2 = mult_tree(trees2)

    print(trees2)

    print(multiple_trees2)


if __name__ == '__main__':
    main()
