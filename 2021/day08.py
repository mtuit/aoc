import collections
import copy
import itertools
import re

numbers = [2, 4, 3, 7]

def read_input(file):
    with open(file) as f: 
        data = f.read().splitlines()
        data = [x.split(' | ') for x in data]
    return data


def solve(data):
    result1 = 0

    for note in data: 
        _, outputs = note[0].split(' '), note[1].strip().split(' ')

        for output in outputs: 
            if len(output) in numbers:
                result1 += 1

    return result1

def solve2(data):
    result = 0

    for note in data: 
        patterns, outputs = note[0].split(' '), note[1].strip().split(' ')

        key_map = collections.defaultdict(int)
        key_map[1] = set([p for p in patterns if len(p) == 2][0])
        key_map[7] = set([p for p in patterns if len(p) == 3][0])
        key_map[4] = set([p for p in patterns if len(p) == 4][0])
        key_map[8] = set([p for p in patterns if len(p) == 7][0])


        for p in map(set, patterns): 
            if len(p) == 5:
                if key_map[7].issubset(p): 
                    key_map[3] = p 
                elif len(key_map[4] & p) == 3: 
                    key_map[5] = p
                else: 
                    key_map[2] = p 
            elif len(p) == 6: 
                if key_map[4].issubset(p):
                    key_map[9] = p 
                elif key_map[7].issubset(p): 
                    key_map[0] = p 
                else: 
                    key_map[6] = p

        result_number = ''
        for o in map(set, outputs): 
            for number, mapping in key_map.items(): 
                if o == mapping: 
                    result_number += str(number)

        result += int(result_number)

    return result

if __name__ == "__main__":
    file = '2021/input/day08.txt'
    data = read_input(file)
    result1, result2 = solve(data), solve2(data)
    print(f"Result for part 1: {result1}\nResult for part 2: {result2}")