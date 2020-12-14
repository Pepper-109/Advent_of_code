import itertools

def puzzle_input():
    with open("Input.txt", 'r') as file:
        lst = [int(i.strip()) for i in file.readlines()]

    return lst

def sum_of_comb(add_lst, num, inval, minim):
    sum_of_lst = []
    count = 0
    for i in itertools.combinations(add_lst, num):
        if inval != -1:
            count += 1
            i = list(i)
            i.sort()
            if i[0] + i[-1] <= minim:
                if sum(i) <= inval:
                    if count % 1000000 == 1:
                        #print("Maybe valid", i)
                        pass
                    if sum(i) == inval:
                        print("Valid", i)
                        sum_of_lst.append(list(i))
        else:
            #print("check")
            sum_of_lst.append(list(i))
    return sum_of_lst

def check_valid(dat, preamble, sum_of):
    for i in range(len(dat)):
        if i > preamble:
            valid = 0
            add_range = dat[i-preamble-1:i-1]
            #print(add_range)
            comb = sum_of_comb(add_range, sum_of, -1, 0)
            #print(comb)
            for num in comb:
                if sum(num) == dat[i-1]:
                    valid = 1
            if valid == 0:
                return [sum_of, preamble, dat[i-1]]

def encryp_weak(to_sum, invalid_num):
    sum_lst = [[0,0], [1,1]]
    to_sum.sort()
    mini = invalid_num
    print(len(to_sum))
    for i in range(2, len(to_sum)):
        print(i)
        comb = sum_of_comb(to_sum[:620], i, invalid_num, mini)
        for i in comb:
            if i[0] + i[-1] < mini:
                print("New mini", i)
                mini = i[0] + i[-1]
    
    return mini

def main():

    data = puzzle_input()

    #print(data)

    first_to_f = check_valid(data, 25, 2)

    print("The first number to not be a sum of", first_to_f[0], "the last", first_to_f[1], "numbers is", first_to_f[2])

    print("\n----------------- Part 2 -----------------\n")

    '''The final step in breaking the XMAS encryption relies on the invalid number you just found: 
        you must find a contiguous set of at least two numbers in your list which sum to 
        the invalid number from step 1.

        In the example list, adding up all of the numbers from 15 through 40 produces 
        the invalid number from step 1, 127. 
        
        (Of course, the contiguous set of numbers in your actual list might be much longer.)

        To find the encryption weakness, add together the smallest and largest number in this contiguous range; 
        in this example, these are 15 and 47, producing 62.'''


    encryption_weakness = encryp_weak(data, first_to_f[2])

    print("The encryption weakness is", encryption_weakness)

    

if __name__ == '__main__':
    main()