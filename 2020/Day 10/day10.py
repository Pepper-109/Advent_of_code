# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 16:25:00 2020

@author: Be_Our_Guest
"""

def puzzle_input():
    '''Formats puzzle input and stores in list, returns said list'''
    with open("test-Input.txt", 'r') as file:
        lst = [int(i.strip()) for i in file.readlines()]
        lst.sort()

    return lst

def adapter_differences(layout, adap_rating):
    adap_difference = []
    for i in range(len(layout)):
        #print(data[i], current_adap_rating)
        #print(adap_diff)
        if layout[i] >= adap_rating -3:
            if layout[i] <= adap_rating + 3:
                adap_difference.append(layout[i] - adap_rating)
                adap_rating = layout[i]
            else:
                print("Adapter", layout[i], "is over joltage from", layout[i-1])
                return False
        else:
            print("Adapter", layout[i], "is under joltage from", layout[i-1])
            return False
    return adap_difference

def valid_adap_layout(layout):
    adap_rating = 0
    for i in range(len(layout)):
        #print(data[i], current_adap_rating)
        #print(adap_diff)
        if not layout[i] >= adap_rating -3:
            #print("Adapter", layout[i], "is under joltage from", layout[i-1])
            return False

        if not layout[i] <= adap_rating + 3:
            #print("Adapter", layout[i], "is over joltage from", layout[i-1])
            return False

        adap_rating = layout[i]

    return True

def main():
    '''

    Any given adapter can take an input 1, 2, or 3 jolts lower than its rating and
    still produce its rated output joltage.

    built-in joltage adapter rated for 3 jolts higher than the highest-rated adapter in your bag. (If your adapter list were 3, 9, and 6, your device's built-in adapter would be rated for 12 jolts.)

    Treat the charging outlet near your seat as having an effective joltage rating of 0.

    If you use every adapter in your bag at once, what is the distribution of joltage differences between the charging outlet, the adapters, and your device?



    test-Input:

        With these adapters, your device's built-in joltage adapter
        would be rated for 19 + 3 = 22 jolts, 3 higher than the highest-rated adapter.

        In this example, when using every adapter,
        there are 7 differences of 1 jolt and 5 differences of 3 jolts.
        '''

    data = puzzle_input()

    adap_diff = [] # Starts at 3 to account for backpack rating
    data.insert(0, 0) # Pos 0 is outlet, outlet has rating of 0
    data.append(data[-1] + 3) # Last position is backpack, rating max + 3

    #print(data)

    adap_diff = adapter_differences(data, data[0])

    print("\nNumber of 0 differences:", adap_diff.count(0) - 1,
          "\nNumber of 1 differences:", adap_diff.count(1),
          "\nNumber of 2 differences:", adap_diff.count(2),
          "\nNumber of 3 differences:", adap_diff.count(3))

    print(adap_diff.count(1) * adap_diff.count(3))


    print("\n------------- Part 2 --------------\n")
    '''

        (0), 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, (22)
        (0), 1, 4, 5, 6, 7, 10, 12, 15, 16, 19, (22)
        (0), 1, 4, 5, 7, 10, 11, 12, 15, 16, 19, (22)
        (0), 1, 4, 5, 7, 10, 12, 15, 16, 19, (22)
        (0), 1, 4, 6, 7, 10, 11, 12, 15, 16, 19, (22)
        (0), 1, 4, 6, 7, 10, 12, 15, 16, 19, (22)
        (0), 1, 4, 7, 10, 11, 12, 15, 16, 19, (22)
        (0), 1, 4, 7, 10, 12, 15, 16, 19, (22)

        Given the adapters from the first example,
        the total number of arrangements that connect the charging outlet to your device is 8.

        Given the adapters from the second example,
        There are 19208 distinct arrangements.

        What is the total number of distinct ways you can arrange
        the adapters to connect the charging outlet to your device?

    '''

    current_adap_rating = data[0]
    arrangements = []
    possible_adap = []
    val_adap = []

    print(data)

    for i in range(len(data)-1):
        #print(data[i], current_adap_rating)
        #print(adap_diff)
        possible_adap = []
        for j in range(i+1, len(data)):
            #print(data[i], data[j])
            if data[i] >= current_adap_rating -3:
                if data[i] <= current_adap_rating + 3:
                    if data[j] <= data[i] + 3 and data[j] >= data[i] -3:
                        #print("Possible")
                        possible_adap.append(data[j])
                    current_adap_rating = data[i]
                else:
                    print("Adapter", data[i], "is over joltage from", data[i-1])
                    break
            else:
                print("Adapter", data[i], "is under joltage from", data[i-1])
                break
        print("Adapter", data[i], "Possble adapters", possible_adap, len(possible_adap))

        val_adap.append(possible_adap)

    print(val_adap)

    print(data)

    for i in range(len(data) - 1):
        #print(data)
        #print(len(data) - 1)
        #print(len(val_adap))
        for j in val_adap[i]:
            #print(data[i], val_adap[i])
            data[i+1:i+len(val_adap[i])+1] = [j]
            #print(data, val_adap[i])
            #val_adap[i], j, data[i+1:i+len(val_adap[i])+1])
            if valid_adap_layout(data):
                arrangements.append(data)
                #print("VALID", data)
            data = puzzle_input()
            data.insert(0, 0)
            data.append(data[-1] + 3)

    print("Valid arrangements")

    arr = []

    for i in arrangements:
        if i not in arr:
            arr.append(i)

    for i in arr:
        print(i)

    #print("\nThe number of unique arrangements for the adapters is", len(arrangements))





if __name__ == '__main__':
    main()