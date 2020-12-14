import collections
import copy
import itertools

def read_input(file):
    with open(file) as f: 
        data = f.read().splitlines()
    return data


def solve(data):
    result1, result2 = (None, None)

    return result1, result2


if __name__ == "__main__":
    file = 'input/day11.txt'
    data = read_input(file)
    result1, result2 = solve(data)
    print(f"Result for part 1: {result1}\nResult for part 2: {result2}")