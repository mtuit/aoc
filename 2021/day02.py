import collections
import copy
import itertools
import re

def read_input(file):
    with open(file) as f: 
        data = f.read().splitlines()
    return data


def solve(data):
    result1, result2 = (None, None)

    depth = 0
    hor_pos = 0
    aim = 0
    for line in data: 
        instruction, value = line.split(" ")
        value = int(value)
        if instruction == "down":
            aim += value
        elif instruction == "up":
            aim -= value
        else:
            hor_pos += value
            depth += aim * value

    result1, result2 = hor_pos * aim, hor_pos * depth 
    return result1, result2


if __name__ == "__main__":
    file = '2021/input/day02.txt'
    data = read_input(file)
    result1, result2 = solve(data)
    print(f"Result for part 1: {result1}\nResult for part 2: {result2}")