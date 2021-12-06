import copy
import itertools
import re
from collections import Counter


def read_input(file):
    with open(file) as f: 
        data = f.read().splitlines()
    return data


def solve(data):
    result1, result2 = (None, None)
    
    gamma = ''
    epsilon = ''
    oxygen_data = copy.deepcopy(data)
    scrubber_data = copy.deepcopy(data)

    for idx in range(len(data[0])): 
        counts = Counter(num[idx] for num in data)
        
        if counts['0'] > counts['1']: 
            gamma += '0'
            epsilon += '1'

        else: 
            gamma += '1'
            epsilon += '0'
            
    for idx in range(len(oxygen_data[0])): 
        if len(oxygen_data) > 1:
            counts = Counter(num[idx] for num in oxygen_data)
            if counts['0'] > counts['1']:
                oxygen_data = [num for num in oxygen_data if num[idx] == '0']
            else: 
                oxygen_data = [num for num in oxygen_data if num[idx] == '1']

    for idx in range(len(scrubber_data[0])): 
            if len(scrubber_data) > 1:
                counts = Counter(num[idx] for num in scrubber_data)
                if counts['0'] > counts['1']:
                    scrubber_data = [num for num in scrubber_data if num[idx] == '1']
                else: 
                    scrubber_data = [num for num in scrubber_data if num[idx] == '0']

    print(oxygen_data, scrubber_data)
    result1 = int(gamma, 2) * int(epsilon, 2)
    result2 = int(oxygen_data[0], 2) * int(scrubber_data[0], 2)
    return result1, result2


if __name__ == "__main__":
    file = '2021/input/day03.txt'
    data = read_input(file)
    result1, result2 = solve(data)
    print(f"Result for part 1: {result1}\nResult for part 2: {result2}")