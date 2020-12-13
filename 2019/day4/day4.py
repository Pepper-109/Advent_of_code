# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 09:51:45 2020

@author: Be_Our_Guest
"""   

def makePasswordList(lower, upper):
    passwords = []
    i = lower
    while i <= upper:
        passwords.append(str(i))
        i += 1
    with open('Full-password-list.txt', 'w') as inp:
        inp.write(str(passwords))
    return passwords

def removeDecending(lst):
    toBeRemoved = []
    for i in lst:
      mini = 0
      if int(i[-1]) < int(i[0]):
          toBeRemoved.append(i)
      else:
          if int(i) % 10001 == 0:
              print(i)
          for j in i:
              if int(j) >= mini:
                  mini = int(j)
              else:
                  toBeRemoved.append(i)
                  break;

    print(toBeRemoved)
    
    for i in toBeRemoved:
        lst.remove(i)
        print("Removing", i)
    
    with open('Not-decending-passwords.txt', 'w') as inp:
        inp.write(str(lst))
        
def findPairs(lst, part):
    if part == 1:
        toBeRemoved = []
        for i in lst:
            pairs = 0
            for j in range(len(i) - 1):
                if i[j] == i[j+1]:
                    pairs += 1
            if pairs == 0:
                toBeRemoved.append(i)
        
        for i in toBeRemoved:
            lst.remove(i)
    else:
        toBeRemoved = []
        for i in lst:
            pairs = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0,}
            for j in range(len(i) - 1):
                if i[j] == i[j+1]:
                    pairs[str(i[j])] += 1
            values = 0
            for key,value in pairs.items():
                if value == 1:
                    values = 1
            
            if values == 0:
                toBeRemoved.append(i)
        
        for i in toBeRemoved:
            lst.remove(i)
    
    return lst
            
    
def main():
    
        
    '''with open('day4-input-part-1.txt', 'r') as inp:
        data = inp.read().split('-')
        
    lower = int(data[0])
    upper = int(data[1])'''
    
    with open('Full-password-list.txt', 'r') as inp:
        passwords = inp.read()
    
    passwords = passwords.replace(']', '')
    passwords = passwords.replace('[', '')
    passwords = passwords.replace('\'', '')
    passwords = passwords.split(', ')
    
    print("Length of all possible passwords:", len(passwords))
    
    '''
        6 digit number
        Value is within range of puzzle input
        At least one pair of the same digit
        Left to right, digits never decrease
      
        How many different passwords within the range given in your puzzle input meet these criteria?
    '''
        
    with open('Not-decending-passwords.txt', 'r') as inp:
        notDecending = inp.read()
    
    notDecending = notDecending.replace(']', '')
    notDecending = notDecending.replace('[', '')
    notDecending = notDecending.replace('\'', '')
    notDecending = notDecending.split(', ')
    
    print("Length of all non decending passwords:", len(notDecending))
    
    pairsAndNotDecending = findPairs(notDecending, 1)
    
    print("Length of all non decending passwords:", len(notDecending))
    
    print("\n--------------------- Part 2 ----------------------\n")
    
    part2 = findPairs(pairsAndNotDecending, 2)
    
    print("Length of all non decending passwords with pairs of length 2:", len(part2))

if __name__ == '__main__':
    main()