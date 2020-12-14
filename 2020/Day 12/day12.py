def puzzle_input():
    with open("test-Input.txt", 'r') as file:
        lst = [i.strip() for i in file.readlines()]

    return lst

def main():
    '''
    Action N means to move north by the given value.
    Action E means to move east by the given value.
    Action S means to move south by the given value.
    Action W means to move west by the given value.
    
    Action L means to turn left (relative to the way point) the given number of degrees.
    Action R means to turn right (relative to the way point) the given number of degrees.
    
    Action F means to move forward by the given value in the direction the ship is currently facing.

    The ship starts by facing east. 
    Only the L and R actions change the direction the ship is facing. 
    (That is, if the ship is facing east and the next instruction is N10, 
    the ship would move north 10 units, but would still move east if the following action were F.)
    '''

    data = puzzle_input()

    #print(data)

    ship_pos = [0, 0] # [ X, Y ] North is y+, East is x+, Right is ship_pos, Left is neg

    heading = 90 # 0° (or 360°) is North, 90° is East, 180° is South, and 270° is West.

    for i in data:
        if i[0] == 'N':
            ship_pos[1] += int(i[1:])
        elif i[0] == 'E':
            ship_pos[0] += int(i[1:])
        elif i[0] == 'S':
            #print("Before", ship_pos, heading, i)
            ship_pos[1] -= int(i[1:])
            #print("Aft", ship_pos, heading, i)
        elif i[0] == 'W':
            ship_pos[0] -= int(i[1:])
        elif i[0] == 'L':
            heading -= int(i[1:])
        elif i[0] == 'R':
            #print("Before", ship_pos, heading, i)
            heading += int(i[1:])
            #print("After", ship_pos, heading, i)
        elif i[0] == 'F':
            #print("Before", ship_pos, heading, i)
            if (heading // 90) % 4 == 0: # Facing North
                ship_pos[1] += int(i[1:])
            elif (heading // 90) % 4 == 1: # Facing East
                ship_pos[0] += int(i[1:])
            elif (heading // 90) % 4 == 2: # Facing South
                ship_pos[1] -= int(i[1:])
            elif (heading // 90) % 4 == 3: # Facing West
                ship_pos[0] -= int(i[1:])
            else:
                print("Didn't turn a full 90 degrees")
                break
            #print("After", ship_pos, heading)
        else:
            print("Direction not recognized!", i)
            break
            

    print("The final ship_position of the ship is", ship_pos, "facing", heading, "from true North")
    print("The Manhattan distance is", abs(ship_pos[0]) + abs(ship_pos[1]))


    print("\n-------------- Part 2 --------------\n")
    '''
    Almost all of the actions indicate how to move a waypoint which is relative to the ship's ship_position:

    Action N means to move the waypoint north by the given value.
    Action S means to move the waypoint south by the given value.
    Action E means to move the waypoint east by the given value.
    Action W means to move the waypoint west by the given value.
    
    Action L means to rotate the waypoint around the ship left (counter-clockwise) the given number of degrees.
    Action R means to rotate the waypoint around the ship right (clockwise) the given number of degrees.
    
    Action F means to move forward to the waypoint a number of times equal to the given value.

    The waypoint starts 10 units east and 1 unit north relative to the ship. 
    The waypoint is relative to the ship; that is, if the ship moves, the waypoint moves with it.
    '''

    ship_pos = [0, 0]
    way_pos = [10, 1]
    way_heading = 0

    for i in data:
        print("Current:", ship_pos, way_pos)
        if i[0] == 'N':
            way_pos[1] += int(i[1:])
        elif i[0] == 'E':
            way_pos[0] += int(i[1:])
        elif i[0] == 'S':
            #print("Before", ship_pos, heading, i)
            way_pos[1] -= int(i[1:])
            #print("Aft", ship_pos, heading, i)
        elif i[0] == 'W':
            way_pos[0] -= int(i[1:])
        elif i[0] == 'L':
            turn_angle = int(i[1:])
            while turn_angle > 0:
                if abs(way_pos[0]) == way_pos[0]:
                    if abs(way_pos[1]) == way_pos[1]: # If x and y are pos
                        way_pos[0] = -way_pos[0]
                    else: # If x is pos and y is neg
                        way_pos[1] = abs(way_pos[1])
                else:
                    if abs(way_pos[1]) == way_pos[1]: # If x is neg and y is pos
                        way_pos[1] = -way_pos[1]
                    else: # If x and y are neg
                        way_pos[0] = abs(way_pos[0])
                turn_angle -= 90
        elif i[0] == 'R':
            #print("Before", ship_pos, heading, i)
            turn_angle = int(i[1:])
            while turn_angle > 0:
                if abs(way_pos[0]) == way_pos[0]:
                    if abs(way_pos[1]) == way_pos[1]: # If x and y are pos
                        way_pos[1] = -way_pos[1]
                    else: # If x is pos and y is neg
                        way_pos[0] = -way_pos[0]
                else:
                    if abs(way_pos[1]) == way_pos[1]: # If x is neg and y is pos
                        way_pos[0] = abs(way_pos[0])
                    else: # If x and y are neg
                        way_pos[1] = abs(way_pos[1])
                turn_angle -= 90
            #print("After", ship_pos, heading, i)
        elif i[0] == 'F':
            #print("Before", ship_pos, way_pos, way_heading, i)
            ship_pos[0] += way_pos[0]*int(i[1:])
            ship_pos[1] += way_pos[1]*int(i[1:])
            #print("After", ship_pos, way_pos, way_heading, i)
        else:
            print("Direction not recognized!", i)
            break



if __name__ == '__main__':
    main()