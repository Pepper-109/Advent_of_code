# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 21:01:35 2020

@author: Be_Our_Guest
"""


def makeCoords(f):
        x = 0
        y = 0
        lst = []
        for i in f:
            if i[0] == 'R':
                x += int(i[1:])
            if i[0] == 'L':
                x -= int(i[1:])
            if i[0] == 'U':
                y += int(i[1:])
            if i[0] == 'D':
                y -= int(i[1:])
            lst.append([x, y])
        return lst

'''Makes a list of places where the lines were vertical'''
def findVerts(f):
        lst = []
        for i in range(len(f)-1):
            if f[i][0] == f[i+1][0]:
                lst.append([f[i], f[i+1]])
        return lst

'''Takes those vertical points, checks them against the other line's horizontal and sees if they can intersect'''
def findPossibleIntersections(coords, verts):
        lst = []
        for i in range(len(coords)-1): #iterates through all coords in line2'''
            if coords[i][0] != coords[i+1][0]: #'if the line segment is moving along the x axis, aka horizontal'''
                for j in verts: #'''check the segment against a vertical line to see if the horizontal line is in the correct y value to intersect'''
                    if min(coords[i][0], coords[i+1][0]) < j[0][0] and max(coords[i][0], coords[i+1][0]) > j[0][0] \
                        and min(j[0][1], j[1][1]) < coords[i][1] and max(j[0][1], j[1][1]) > coords[i][1]:
                            lst.append([j, [coords[i], coords[i+1]]])
        return lst

'''For each possible intersection line segment, iterate through all points on that segment and find intersection'''
def findAllPointsOnSegment(inter):
    lst = []
    for i in inter:
        line1 = []
        line2 = []
        if i[0][0][1] > i[0][1][1]:
            line1.append(i[0][0])
            x = i[0][0][0]
            y = i[0][0][1]
            for j in range(abs(i[0][0][1] - i[0][1][1])):
                y -= 1
                line1.append([x, y])
        else:
            line2.append(i[0][1])
            x = i[0][0][0]
            y = i[0][1][1]
            for j in range(abs(i[0][0][1] - i[0][1][1])):
                y -= 1
                line1.append([x, y])
        if i[1][0][0] > i[1][1][0]:
            line2.append(i[1][0])
            x = i[1][0][0]
            y = i[1][0][1]
            for j in range(abs(i[1][0][0] - i[1][1][0])):
                x -= 1
                line2.append([x, y])
        else:
            line2.append(i[1][1])
            x = i[1][1][0]
            y = i[1][0][1]
            for j in range(abs(i[1][0][0] - i[1][1][0])):
                x -= 1
                line2.append([x, y])
        for i in line1:
            if i in line2:
               lst.append(i)
    return lst


def main():
    t1 = "R8,U5,L5,D3".split(',') #Change this later to pull from file
    t2 = "U7,R6,D4,L4".split(',')
    
    t1coord = []
    t2coord = []
    
    t1coord = makeCoords(t1)
    t2coord = makeCoords(t2)
    
    print("t1coord", t1coord)
    print("t2coord", t2coord)
    
    vert1 = findVerts(t1coord)
    vert2 = findVerts(t2coord)
    
    inter = findPossibleIntersections(t1coord, vert2)
    
    inter.extend(findPossibleIntersections(t2coord, vert1))
    
    print("possible intersections", inter)
    
    cross = findAllPointsOnSegment(inter)
    
    print("Intersection points", cross)
    
    mini = abs(cross[0][0]) + abs(cross[0][1])
    
    for i in cross:
        if (abs(i[0]) + abs(i[1])) < mini:
            mini = abs(i[0]) + abs(i[1])
    
    
    print(mini)
    

'''Checks to see if the file is running directly,
if it is then run everything in Main,
if it is not (aka being imported by another file),
don't run Main and instead only run functions that get called'''

if __name__ == '__main__':
  main()
  








