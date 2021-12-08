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

    # mapping = collections.defaultdict(int)
    for note in data: 
        patterns, outputs = note[0].split(' '), note[1].strip().split(' ')

        for output in outputs: 
            if len(output) in numbers:
                result1 += 1

    return result1


wire_mapping = collections.defaultdict(str)
number_mapping = collections.defaultdict(int)

def solve2(data):
    result = None
    
    for note in data: 
        patterns, outputs = note[0].split(' '), note[1].strip().split(' ')

        patterns.sort(key=len)
        for pattern in patterns: 
            

            break

    return result

if __name__ == "__main__":
    file = '2021/input/day08.txt'
    data = read_input(file)
    result1, result2 = solve(data), solve2(data)
    print(f"Result for part 1: {result1}\nResult for part 2: {result2}")