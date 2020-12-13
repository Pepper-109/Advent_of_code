def puzzle_input():
    with open("test-Input.txt", 'r') as file:
        lst = [i.strip().replace('.', '').replace('no', '0') for i in file.readlines()]

    for i in range(len(lst)):
        lst[i] = lst[i].split(" bags ")

    return lst

def recursive_shiny_check(dat, shiny_list):
    for bag in range(len(dat)):
        for i in dat:
            for j in shiny_list:
                #print("Bag", i[0], "contains", i[1])
                #print("Bags that can contain shinies:", j)
                if j in i[1] and i[0] not in shiny_list:
                    #print(i[0], "can contain a shiny gold bag")
                    shiny_list.append(i[0])
                    break
    return shiny_list

def how_many_bags(bag):
        num = ''
        for char in bag:
            if char != ' ':                    
                num = num + char                  
            else:
                return num

def main():
    ''' light red bags contain 1 bright white bag, 2 muted yellow bags.
        dark orange bags contain 3 bright white bags, 4 muted yellow bags.
        bright white bags contain 1 shiny gold bag.
        muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
        shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
        dark olive bags contain 3 faded blue bags, 4 dotted black bags.
        vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
        faded blue bags contain no other bags.
        dotted black bags contain no other bags.
        
        These rules specify the required contents for 9 bag types. 
        In this example, every faded blue bag is empty, every vibrant plum bag contains 11 bags (5 faded blue and 6 dotted black), and so on.
        
        A bright white bag, which can hold your shiny gold bag directly.
        A muted yellow bag, which can hold your shiny gold bag directly, plus some other bags.
        A dark orange bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
        A light red bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
        
        So, in this example, the number of bag colors that can eventually contain at least one shiny gold bag is 4.
        
        How many bag colors can eventually contain at least one shiny gold bag?'''

    data = puzzle_input()

    #print("Data", data)

    contains_shiny = []

    for i in data:
        if 'shiny gold' in i[1] and i[0] not in contains_shiny:
            #print("Bag", i[0], "contains", i[1])
            contains_shiny.append(i[0])

    print("\nContains shiny directly", contains_shiny)

    contains_shiny = recursive_shiny_check(data, contains_shiny)
    
    print("\nContains shiny indirectly or directly", len(contains_shiny))

    print("\n------------------- Part 2 -------------------\n")

    '''shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
        faded blue bags contain 0 other bags.
        dotted black bags contain 0 other bags.
        vibrant plum bags contain 11 other bags: 5 faded blue bags and 6 dotted black bags.
        dark olive bags contain 7 other bags: 3 faded blue bags and 4 dotted black bags.
    
        So, a single shiny gold bag must contain 1 dark olive bag (and the 7 bags within it) 
        plus 2 vibrant plum bags (and the 11 bags within each of those): 
        1 + 1*7 + 2 + 2*11 = 32 bags!'''

    gold_contains = {}

    for i in data:
        #print(i[1])
        i[1] = i[1].replace('contain ', '')
        #print(i[1])
        i[1] = i[1].split(', ')
       
        #print(i)
        #print(i[1])
        gold_contains[i[0]] = {}
        for bags in range(len(i[1])):
            #print("BAG", i[1][bags])
            num_bag = how_many_bags(i[1][bags])
            #print(num_bag)
            i[1][bags] = i[1][bags].split(num_bag + ' ')
            i[1][bags] = i[1][bags][1]
            i[1][bags] = i[1][bags].replace(' bags', '')
            i[1][bags] = i[1][bags].replace(' bag', '')
            #print("BAGS", i[1][bags])
            
            #print(i)
            if num_bag == '0':
                break
                # gold_contains[i[0]][i[1][bags]] = {}
            else:
                gold_contains[i[0]][i[1][bags]] = int(num_bag)

    new = 0
    old = 1
    count = 0
    count2 = 0

    print("Shiny gold bag contains", gold_contains)

    stack = [{"shiny gold": 1}]

    while stack:
        to_process = stack.pop(0)
        print("To proc", to_process.keys())
        for i in to_process.keys():
            stack.append(gold_contains[i])
        print(stack)


    '''while new != old:
        old = len(gold_contains)
        for i in data:
            if i[0] != 'shiny gold':
                #print(i)
                #print(i[1])
                #print(i)
                for j in range(len(gold_contains)):
                    count2 = gold_contains[j][0]
                    #print(gold_contains)
                    #print(count2)
                    #print(len(gold_contains))
                    #print(i)
                    #print("Bag", i[0], "contains", i[1])
                    #print("Bags that can contain shinies:", j)
                    #print(j[1])
                    #print(i[0])
                    gold_contains2 = []
                    for k in gold_contains:
                        gold_contains2.append(k[1])
                    #print("gold2", gold_contains2)
                    #print(i[0])
                    br = 0
                    #print(count)
                    #print(j)
                    #print(count)
                    #print(gold_contains[j][1])
                    #print(i[0])
                    if gold_contains[j][1] == i[0] and i[0] in gold_contains2 and j == count:
                        #print("Shiny gold bag contains", i[0], gold_contains)
                        for bags in range(len(i[1])):
                            #print(i[1])
                            #print("First go", i[1][bags])
                            num_bag = how_many_bags(i[1][bags])
                            if num_bag == '0':
                                br = 1
                                break
                            #print("bags", num_bag, "amount", count2)
                            #print(i)
                            gold_contains.append([int(num_bag)*count2, i[1][bags].replace(' bags', '').split(num_bag + ' ')[1]])
                        #print(gold_contains)
                    if br == 1:
                        break
        new = len(gold_contains)
        count += 1

    print(gold_contains)

    summ = 0

    for i in gold_contains:
        summ += i[0]

    print(summ)


    #print(data)'''


if __name__ == '__main__':
    main()