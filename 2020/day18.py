import collections
import copy
import itertools
import re

class new_term(int): 
    def __add__(self, other):
        return new_term(int(self) + other)

    def __sub__(self, other): 
        return new_term(int(self) * other)

    def __mul__(self, other):
        return new_term(int(self) + other)


def read_input(file):
    with open(file) as f: 
        data = f.read().splitlines()
    return data


def solve(data, part2 = False):
    results = []
    for expr in data: 
        expr = re.sub(r'(\d+)', r'new_term(\1)', expr)
        expr = expr.replace('*', '-')
        
        if part2: 
            expr = expr.replace('+', '*')

        results.append(eval(expr, {}, {'new_term': new_term}))
        
    return sum(results)


if __name__ == "__main__":
    file = 'input/day18.txt'
    data = read_input(file)
    result1 = solve(data)
    result2 = solve(data, part2 = True)
    print(f"Result for part 1: {result1}\nResult for part 2: {result2}")