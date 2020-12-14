import collections
import copy
import itertools
import re

def read_input(file):
    with open(file) as f: 
        data = f.read().splitlines()
    return data


def apply_mask(value, mask):
    value = value | int(mask.replace('X', '0'), 2)
    value = value & int(mask.replace('X', '1'), 2)
    return value


def get_addresses(address):
    return itertools.product('01', repeat=address.count('X'))


def solve(data):
    result1, result2 = (None, None)
    curr_mask = None
    mem1 = collections.defaultdict(int)
    mem2 = collections.defaultdict(int)
    for instruction in data: 
        instr, value = instruction.split(' = ')

        if instr == 'mask': 
            curr_mask = value
        else: 
            address = instr[4:-1]
            mem1[address] = apply_mask(int(value), curr_mask)

            address_bit = f'{int(address):036b}'
            address_masked = [address_bit[idx] if bit == '0' else bit for idx, bit in enumerate(curr_mask)]

            for new_bits in get_addresses(address_masked):
                new_bits = iter(new_bits)
                addr = ''.join([next(new_bits) if char == 'X' else char for char in address_masked])
                mem2[int(addr, 2)] = int(value)

    result1 = sum(mem1.values())
    result2 = sum(mem2.values())
    return result1, result2


if __name__ == "__main__":
    file = 'input/day14.txt'
    data = read_input(file)



    result1, result2 = solve(data)
    print(f"Result for part 1: {result1}\nResult for part 2: {result2}")