import collections

def read_input(file):
    with open(file) as f: 
        data = f.read().splitlines()
    return data


def build_bag_trees(data): 
    holds = collections.defaultdict(list)
    is_held_by = collections.defaultdict(set)

    for line in data: 
        bag = ' '.join(line.split(' ')[0:2])
        line = ' '.join(line.split(' ')[4:])

        if ',' in line: 
            inner_bags = line.split(', ')
        else: 
            inner_bags = [line]
        
        for inner_bag in inner_bags: 
            if inner_bag[0] != 'n':
                number = int(inner_bag[0])
                inner_bag = ' '.join(inner_bag.split(' ')[1:3])
                holds[bag].append((number, inner_bag))
                is_held_by[inner_bag].add(bag)

    return holds, is_held_by


def check_bag(bag, is_held_by, accumulator):
    for hold_bag in is_held_by[bag]:
        accumulator.add(hold_bag)
        check_bag(hold_bag, is_held_by, accumulator)

    return accumulator


def cost_of_bag(bag, holds):
    total = 0

    for cost, inner_bag in holds[bag]:
        total += cost
        total += cost * cost_of_bag(inner_bag, holds)

    return total

if __name__ == "__main__":
    file = 'input/day07.txt'
    data = read_input(file)
    holds, is_held_by = build_bag_trees(data)

    result1 = len(check_bag('shiny gold', is_held_by, set()))
    result2 = cost_of_bag('shiny gold', holds)

    print(f"Result for part 1: {result1}\nResult for part 2: {result2}")