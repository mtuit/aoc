import collections
import copy
import itertools
import re

def read_input(file):
    with open(file) as f: 
        data = f.read()
        data = [*map(int, data.split(','))]
    return data


def solve(data):
    lowest = 0
    
    for i in range(min(data), max(data)): 
        current_fuel = 0
        for crab in data: 
            current_fuel += abs(crab - i)
        if current_fuel < lowest or lowest == 0: 
            lowest = current_fuel
            
    return lowest


def solve2(data):
    lowest = 0

    for i in range(min(data), max(data)): 
        current_fuel = 0
        for crab in data: 
            difference = abs(crab - i)
            current_fuel += sum(range(difference + 1))
        if current_fuel < lowest or lowest == 0: 
            lowest = current_fuel

    return lowest


if __name__ == "__main__":
    file = '2021/input/day07.txt'
    data = read_input(file)
    result1, result2 = solve(data), solve2(data)
    print(f"Result for part 1: {result1}\nResult for part 2: {result2}")
