import math
import itertools

def read_input(file):
    with open(file) as f: 
        data = f.read().splitlines()
    return data

def check_pass_binary(p, lower, upper, up_char, down_char): 
    number = None

    for char in p: 
        if char == up_char: 
            lower += math.ceil((upper - lower) / 2)
            number = lower
        elif char == down_char: 
            upper -= math.ceil((upper - lower) / 2)
            number = upper
    
    return number

def check_passes(passes): 
    seat_ids = []
    for p in passes: 
        row, col = check_pass_binary(p, 0, 127, 'B', 'F'), check_pass_binary(p, 0, 7, 'R', 'L')
        seat_ids.append(row * 8 + col)

    for seat_id in range(256 * 8): 
        if seat_id not in seat_ids and seat_id + 1 in seat_ids and seat_id - 1 in seat_ids: 
            own_seat = seat_id

    return max(seat_ids), own_seat

if __name__ == "__main__":
    file = 'input/day05.txt'
    data = read_input(file)
    result1, result2 = check_passes(data)
    print(f"Result for part 1: {result1}\nResult for part 2: {result2}")