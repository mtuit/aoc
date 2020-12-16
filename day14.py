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


def get_masks_generator(mask): 
    if not mask:
        yield ''
        return
    else: 
        for msk in get_masks_generator(mask[1:]): 
            if mask[0] == 'X': 
                yield '0' + msk
                yield '1' + msk
            elif mask[0] == '1': 
                yield '1' + msk
            elif mask[0] == '0': 
                yield 'X' + msk
            

def solve(data):
    result1, result2 = (None, None)
    mask = None
    mem1 = collections.defaultdict(int)
    mem2 = collections.defaultdict(int)

    for instruction in data: 
        instr, value = instruction.split(' = ')

        if instr == 'mask': 
            mask = value
        else: 
            address, value = int(instr[4:-1]), int(value)
            mem1[address] = apply_mask(value, mask)

            # # Solve by creating new addresses
            # address_bit = f'{address:036b}'
            # address_masked = [address_bit[idx] if bit == '0' else bit for idx, bit in enumerate(mask)]

            # for new_bits in get_addresses(address_masked):
            #     new_bits = iter(new_bits)
            #     addr = ''.join([next(new_bits) if char == 'X' else char for char in address_masked])
            #     mem2[int(addr, 2)] = value

            # Solve by creatings masks which are similar to part 1 so we can re-use code. 
            # Personally I like this solution better than the one I wrote during the puzzle. 
            for msk in get_masks_generator(mask): 
                mem2[apply_mask(address, msk)] = value

    result1 = sum(mem1.values())
    result2 = sum(mem2.values())
    return result1, result2


if __name__ == "__main__":
    file = 'input/day14.txt'
    data = read_input(file)



    result1, result2 = solve(data)
    print(f"Result for part 1: {result1}\nResult for part 2: {result2}")