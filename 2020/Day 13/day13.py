from time import perf_counter

def puzzle_input():
    with open("test-Input6.txt", 'r') as file:
        lst = [i.strip().split(',') for i in file.readlines()]

    return lst

def get_active_buses(dat):
    sched = []

    for i in dat[1]:
        if i != 'x':
            sched.append(int(i))
    
    return sched

def main():
    start = perf_counter()
    '''
    Each bus has an ID number that also indicates how often the bus leaves for the airport.

    What is the ID of the earliest bus you can take to the airport 
    multiplied by the number of minutes you'll need to wait for that bus?    
    '''

    data = puzzle_input()

    #print(data)

    depart_after = int(data[0][0])

    active_buses = get_active_buses(data)

    print("The earliest time you can leave is", depart_after)
    print("\nThe current active buses are", active_buses)

    time = depart_after

    catch_the_bus = []

    for i in active_buses:
        while True:
            if time % i == 0:
                catch_the_bus.append([i, time])
                break
            time += 1
        time = depart_after

    catch_the_bus.sort(key = lambda x: x[1]) # Sorts by the second index, in this case time in minutes

    waiting = catch_the_bus[0][1] - depart_after
    
    print("\nThe earliest bus you can catch is ID", catch_the_bus[0][0], 
        "after waiting for", waiting, "minutes.")

    print("Answer:", catch_the_bus[0][0]*waiting)

    print("\n------------ Part 2 ------------\n")
    '''
    (The first line in your input is no longer relevant.)

    7,13,x,x,59,x,31,19

    This means you are looking for the earliest timestamp (called t) such that:

        Bus ID 7 departs at timestamp t.
        Bus ID 13 departs one minute after timestamp t.
        
        There are no requirements or restrictions on departures at two or three minutes after timestamp t.
        
        Bus ID 59 departs four minutes after timestamp t.
        
        There are no requirements or restrictions on departures at five minutes after timestamp t.
        
        Bus ID 31 departs six minutes after timestamp t.
        Bus ID 19 departs seven minutes after timestamp t.
    '''

    print(data)

    constraints = []

    for i in range(len(data[1])):
        #print(data[1][i])
        if data[1][i] != 'x':
            constraints.append([i, int(data[1][i])])

    constraints.sort(key = lambda x: x[1]) # Sorts by the second index, in this case time in minutes

    print(constraints)

    time_inc = constraints[-1] # Sets the time increment to the largest bus id list
    current_time = 0
    #current_time = 100000000000000 # For puzzle input
    
    print(current_time)
    print(time_inc)

    check = 0

    while check != len(constraints):
        check = 0
        current_time += time_inc[1]
        if current_time % 1000000 == 0:
            print(current_time)
        #if current_time > 1000000:
        #    print(current_time)
        for i in constraints:
            #print(i)
            if not (current_time + (i[0] - time_inc[0])) % i[1] == 0: # Adjusts for time inc offset
                break
            else:
                check += 1
        
    
    print("Earliest time", current_time - time_inc[0])

    print(perf_counter() - start)



if __name__ == '__main__':
    main()