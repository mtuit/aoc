import collections
import copy
import itertools
import re
import numpy as np 

def read_input(file):
    with open(file) as f: 
        data = f.read().split('\n\n')
        numbers, boards = data[0], data[1:]
        numbers = [*map(int, numbers.split(','))]
        boards = np.array([np.genfromtxt(board.split('\n')) for board in boards])
    return numbers, boards


def solve(numbers, boards):
    result1, result2 = (None, None)

    for number in numbers:
        boards[boards == number] = 0
        marked = (boards == 0)
        winner = np.any((np.all(marked, axis=1) | np.all(marked, axis=2)), axis=1)
        
        if np.any(winner): 
            if result1 is not None: 
                result2 = int(boards[winner].sum() * number)
            else: 
                result1 = int(boards[winner].sum() * number)
            boards = boards[~winner]
    
    return result1, result2


if __name__ == "__main__":
    file = '2021/input/day04.txt'
    numbers, boards = read_input(file)
    result1, result2 = solve(numbers, boards)
    print(f"Result for part 1: {result1}\nResult for part 2: {result2}")