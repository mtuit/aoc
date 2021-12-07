import collections
import copy
import itertools
import re
import numpy as np

def read_input(file):
    with open(file) as f: 
        data = f.read()
        data = re.compile(r'(\d+),(\d+) -> (\d+),(\d+)').findall(data)
        data = [tuple(map(int, line)) for line in data]
    return data


def solve(data):
    result1, result2 = (None, None)
    grid = np.zeros(shape=(2, 10000, 10000))

    for x1, y1, x2, y2 in data: 
        sign_x, sign_y = np.sign([x2 - x1, y2 - y1])
        if x1 == x2:
            grid[0, x1, min(y1, y2):max(y1, y2) + 1] += 1
        elif y1 == y2:
            grid[0, min(x1, x2):max(x1, x2) + 1, y1] += 1
        else: 
            while (x1, y1) != (x2 + sign_x, y2 + sign_y): 
                grid[1, x1, y1] += 1
                x1, y1 = x1 + sign_x, y1 + sign_y

    result1 = (grid[0] >= 2).sum()
    result2 = (grid.sum(0) >= 2).sum()
    return result1, result2


if __name__ == "__main__":
    file = '2021/input/day05.txt'
    data = read_input(file)
    result1, result2 = solve(data)
    print(f"Result for part 1: {result1}\nResult for part 2: {result2}")