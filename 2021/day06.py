from collections import Counter, defaultdict
import copy
import itertools
import re
import math

def read_input(file):
    with open(file) as f: 
        data = f.read().split(',')
        data = [*map(int, data)]
    return data


def solve_naive(data, days):
    while days != 0: 
        for idx in range(len(data)):
            data[idx] -= 1
            if data[idx] == -1: 
                data.append(8)
                data[idx] = 6

        days -= 1
        print(days)

    return len(data)

def solve_smart(data, days): 
    result1 = None
    fishes = Counter(data)

    for day in range(days):
        spawn_amount = fishes[0]

        for key in range(0, 9):
            fishes[key] = fishes[key+1]
        fishes[6] += spawn_amount
        fishes[8] = spawn_amount

        if day == 79:
            result1 = sum(fishes.values())
    return result1, sum(fishes.values())

if __name__ == "__main__":
    file = '2021/input/day06.txt'
    data = read_input(file)
    result1, result2 = solve_smart(data, 256)
    print(f"Result for part 1: {result1}\nResult for part 2: {result2}")