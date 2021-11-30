import collections
import copy
import itertools

def read_input(file):
    with open(file) as f: 
        data = [list(row) for row in f.read().split('\n')]
    return data


def valid_position(row_idx, col_idx, row_length, col_length): 
    return 0 <= row_idx < row_length and 0 <= col_idx < col_length


def step(data, adjacent_only=True):
    new_data = copy.deepcopy(data)
    row_length = len(data)
    col_length = len(data[0])

    for row_idx, row in enumerate(data):
        for col_idx, seat in enumerate(row): 
            neighbours = []

            for x in (-1, 0, 1):
                for y in (-1, 0, 1):
                    if x == y == 0:
                        continue
                    
                    if adjacent_only: 
                        if valid_position(row_idx+x, col_idx+y, row_length, col_length):
                            neighbours.append(data[row_idx+x][col_idx+y])
                    else: 
                        i = 1
                        while valid_position(row_idx + i*x, col_idx + i*y, row_length, col_length):
                            char = data[row_idx+i*x][col_idx+i*y]
                            if char != '.':
                                neighbours.append(char)
                                break
                            i += 1

            if adjacent_only: 
                upper_bound = 4
            else: 
                upper_bound = 5

            if seat == 'L' and '#' not in neighbours: 
                new_data[row_idx][col_idx] = '#'
            elif seat == '#' and neighbours.count('#') >= upper_bound: 
                new_data[row_idx][col_idx] = 'L'

    return new_data


def solve(data):
    result1, result2 = (None, None)
    
    last_seating = copy.deepcopy(data)
    curr_seating = None
    while True: 
        curr_seating = step(last_seating)

        if curr_seating == last_seating: 
            count = collections.Counter((seat for row in curr_seating for seat in row))
            result1 = count['#']
            break

        last_seating = copy.deepcopy(curr_seating)

    last_seating = copy.deepcopy(data)
    curr_seating = None   
    while True: 
        curr_seating = step(last_seating, adjacent_only=False)

        if curr_seating == last_seating: 
            count = collections.Counter((seat for row in curr_seating for seat in row))
            result2 = count['#']
            return result1, result2

        last_seating = copy.deepcopy(curr_seating)

    return result1, result2


if __name__ == "__main__":
    file = 'input/day11.txt'
    data = read_input(file)
    result1, result2 = solve(data)
    print(f"Result for part 1: {result1}\nResult for part 2: {result2}")