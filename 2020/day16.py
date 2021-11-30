import collections
import copy
import itertools
import re

def read_input(file):
    with open(file) as f: 
        data = f.read().split('\n\n')
    return data


def solve(data):
    result1, result2 = (None, 1)
    valid, my_ticket, other_tickets = data[0], data[1].split('\n')[1], data[2]
    my_ticket = [int(x) for x in my_ticket.split(',')]
    matches = re.findall(r'\w+:\s(\d+-\d+)\s\w+\s(\d+-\d+)', valid)
    fields = re.findall(r'([a-z]+(?:\s[a-z]+)*):', valid)

    ranges = [number_range.split('-') for match in matches for number_range in match]

    valid_numbers = set()
    valid_range_field = {}
    valid_tickets, invalid_fields = [], []
    valid_positions = collections.defaultdict(list)
    
    for idx in range(0, len(ranges), 2): 
        valid = list(range(int(ranges[idx][0]), int(ranges[idx][1])+1)) + list(range(int(ranges[idx+1][0]), int(ranges[idx+1][1])+1))
        for number in valid: 
            valid_numbers.add(number)

        valid_range_field[fields[int(idx/2)]] = valid


    for ticket in other_tickets.splitlines()[1:]:
        ticket = ticket.split(',')
        
        for field in ticket: 
            if int(field) not in valid_numbers:
                invalid_fields.append(int(field))
        
        if all(int(field) in valid_numbers for field in ticket): 
            valid_tickets.append(ticket)

    result1 = sum(invalid_fields)

    for field, values in valid_range_field.items(): 
        for idx, col in enumerate(zip(*valid_tickets)): 
            if all(int(number) in values for number in col):
                valid_positions[field].append(idx)


    positions_found = [] 
    ticket_positions = {}
    while True: 
        for i in range(1, 21):
            for key, values in valid_positions.items(): 
                if len(values) == i: 
                    for value in values: 
                        if value not in positions_found: 
                            ticket_positions[key] = value
                            positions_found.append(value)
   
        if len(positions_found) == 20: 
            break

    result2 = 1
    for pos, col in ticket_positions.items(): 
        if pos.startswith('departure'): 
            result2 *= int(my_ticket[col])

    return result1, result2


if __name__ == "__main__":
    file = 'input/day16.txt'
    data = read_input(file)
    result1, result2 = solve(data)
    print(f"Result for part 1: {result1}\nResult for part 2: {result2}")