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

    #contains_shiny = recursive_shiny_check(data, contains_shiny)

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

    formatted_data = []

    for i in data:
        #print(i[1])
        i[1] = i[1].replace('contain ', '')
        i[1] = i[1].replace(' bags', '')
        i[1] = i[1].replace(' bag', '')
        #print(i[1])
        i[1] = i[1].split(', ')
        #print(i)
        if i[0] == 'posh blue':
            print(i[1])
        #gold_contains[i[0]] = []
        to_app = []
        for bags in range(len(i[1])):
            #print("BAG", i[1][bags])
            num_bag = how_many_bags(i[1][bags])
            #print(num_bag)
            i[1][bags] = i[1][bags].split(num_bag + ' ')
            i[1][bags] = i[1][bags][1]
            to_app.append([int(num_bag), i[1][bags]])
            if i[0] == 'posh blue':
                print([i[0], int(num_bag), i[1][bags]])
                print(to_app)
            #print("BAGS", i[1][bags])
        formatted_data.append([i[0], to_app])

    count = 0
    count2 = 0
    gold_contains = []
    for i in formatted_data:
        #print("I10", i[1][0][0])
        if i[1][0][0] == 0:
            #print("OTHER", i)
            i[1] = []
            #print(i)
        if i[0] == 'shiny gold':
            gold_contains.append(i[1])

    #print("Shiny gold bag contains", formatted_data)
    pr = 0
    print("Data 0", formatted_data[0])
    print("Gold contains", gold_contains)

    while count < len(data):
        for i in data:
            pass
            #print(i)
        count += 1

    '''while count < len(data):
        #old = len(gold_contains)
        for i in data:
            #print(i[1])
            #print(i)
            for j in range(len(formatted_data)):
                count2 = formatted_data[j][0]
                if count < 13:
                    pass
                    #print(gold_contains)
                    #print("Actual count", count)
                    #print("Count", gold_contains[count:])
                #print(len(gold_contains))
                #print(i)
                #print("Bag", i[0], "contains", i[1])
                #print("Bags that can contain shinies:", j)
                #print(j[1])
                #print(i[0])
                gold_contains2 = []
                for k in formatted_data:
                    gold_contains2.append(k[1])
                if pr == 0:
                    #print("gold2", gold_contains2)
                    #print(gold_contains[j][1], i[0], gold_contains[j][1] == i[0], i[0] in gold_contains2)
                    #print("count", count, j)
                    pr = 1
                #print(i[0])

                #print(count)
                if formatted_data[j][1] == i[0] and i[0] in gold_contains2 and j == count:
                    #print("Shiny gold bag contains", i[0], gold_contains)
                    for bags in range(len(i[1])):
                        #print(i[1])
                        #print(i[1])
                        #print("First go", i[1][bags])
                        num_bag = how_many_bags(i[1][bags])
                        if num_bag == '0':
                            break
                        #print("bags", num_bag, "amount", count2)
                        #print(i)
                        i[1][bags].replace(' bags', '')
                        i[1][bags].replace(' bag', '')
                        formatted_data.append([int(num_bag)*count2, i[1][bags].split(num_bag + ' ')[1]])
                    #print(gold_contains)
        #new = len(gold_contains)
        count += 1
        #print(round(time.perf_counter() - tic, 4), count, "/", len(data))

    print(formatted_data)

    summ = 0

    for i in formatted_data:
        summ += i[0]

    print(summ)'''


    #print(data)


if __name__ == '__main__':
    main()