import collections
import copy
import itertools
import math

from sympy.ntheory.modular import crt
from functools import reduce

def read_input(file):
    with open(file) as f: 
        data = f.read().splitlines()
    return data


# Chinese Remainder implementation using from (https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6)
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


def solve(timestamp, busses):
    least_diff = None
    bus_id = None
    for bus in busses: 
        diff = math.ceil(timestamp / bus) * bus - timestamp

        if least_diff is None: 
            least_diff = diff
            bus_id = bus
        elif diff < least_diff: 
            least_diff = diff
            bus_id = bus

    result1 = least_diff * bus_id
    return result1


def solve2(timestamp, busses): 
    result2 = 0
    n = []
    a = []

    for idx, bus in enumerate(busses): 
        if bus == 'x': 
            continue
        
        n.append(int(bus))
        a.append((int(bus) - idx))

    result2 = chinese_remainder(n, a)
    return result2


# Dirty cheating solution for part 2 using SymPy library, used this to solve the problem quickly but feld like cheating, so wrote solution using CRT as well.
def cheating_solve_part2(data): 
    m, v = zip(*((int(bus), int(bus)-idx) for idx, bus in enumerate(data[1].split(',')) if bus != 'x'))
    return min(crt(m, v))


if __name__ == "__main__":
    file = 'input/day13.txt'
    data = read_input(file)
    timestamp = int(data[0])
    busses = [int(bus) for bus in data[1].split(',') if bus != 'x']
    busses_with_x = data[1].split(',')
    result1 = solve(timestamp, busses)
    result2 = solve2(0, busses_with_x)
    print(f"Result for part 1: {result1}\nResult for part 2: {result2}")