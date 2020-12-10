import itertools
import collections

def read_input(file):
    return list(map(int, open(file)))


def valid_perm(perm):
    if all((number+1==perm[idx+1] or number+3==perm[idx+1]) for idx, number in enumerate(perm) if idx < len(perm)-1):
        return True
    else: 
        return False

            
def solve(data):
    
    result1 = None
    result2 = None
    jolts1 = [1]
    jolts3 = []
    data.sort()

    for idx, adapter in enumerate(data): 
        if idx == len(data)-1: 
            jolts3.append(1)
        elif (adapter + 1) == data[idx+1]: 
            jolts1.append(1)
        elif adapter + 3 == data[idx+1]: 
            jolts3.append(1)
        else: 
            print(f"Current adapter{idx}, {adapter}.")


    result1 = len(jolts1) * len(jolts3)

    # possible_sub = []
    # possible_sub.append((0,))
    # results = []
    # for idx, number in enumerate(data):
    #     new_posses = []
    #     for poss in possible_sub: 
    #         prev_number = poss[-1]

    #         if number-1 == prev_number or number-3 <= prev_number:
    #             new_poss = poss + (number,)
    #             new_posses.append(new_poss)
            
    #     possible_sub.extend(new_posses)
    # result2 = len(list(filter(lambda x: x[-1] == max(data), iter(possible_sub))))


    possibilities = collections.defaultdict(int)
    possibilities[0] = 1
    for number in data: 
        possibilities[number] = possibilities[number-1] + possibilities[number-2] + possibilities[number-3]
    
    result2 = possibilities[max(data)]
    return result1, result2

if __name__ == "__main__":
    file = 'input/day10.txt'
    data = read_input(file)
    result1, result2 = solve(data)
    print(f"Result for part 1: {result1}\nResult for part 2: {result2}")