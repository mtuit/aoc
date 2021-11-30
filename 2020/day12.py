import collections
import copy
import itertools


DIRECTIONS = ['N', 'E', 'S', 'W']
CHANGE = ['R', 'L']


def read_input(file):
    with open(file) as f: 
        data = f.read().splitlines()
    return data


def change_position(curr_direction, action, units): 
    units = int(units / 90)
    idx = DIRECTIONS.index(curr_direction)
    if action == 'R':
        new_direction = DIRECTIONS[(idx + units) % 4]
    elif action == 'L':
        new_direction = DIRECTIONS[(idx - units) % 4]
    return new_direction


def solve(data, start_direction):
    result1 = None
    positions = collections.defaultdict(int)
    curr_direction = start_direction

    for instruction in data: 
        action, units = instruction[0], int(instruction[1:])
        if action in DIRECTIONS: 
            positions[action] += units
        elif action in CHANGE: 
            curr_direction = change_position(curr_direction, action, units)
        elif action == 'F':
            positions[curr_direction] += units

    result1 = abs(positions['N'] - positions['S']) + abs(positions['E'] - positions['W'])
    return result1


def change_waypoint(waypoint, action, units):
    new_waypoint = collections.defaultdict(int)
    units = int(units / 90)

    for idx, direction in enumerate(DIRECTIONS): 
        if action == 'R':
            new_idx = (idx - units) % 4
        elif action == 'L':
            new_idx = (idx + units) % 4
        new_waypoint[direction] = waypoint[DIRECTIONS[new_idx]]

    return new_waypoint


def solve2(data, start_waypoint):
    result2 = None
    positions = collections.defaultdict(int)
    curr_waypoint = start_waypoint

    for instruction in data: 
        action, units = instruction[0], int(instruction[1:])
        if action in DIRECTIONS: 
            curr_waypoint[action] += units
        elif action in CHANGE: 
            curr_waypoint = change_waypoint(curr_waypoint, action, units)
        elif action == 'F':
            for direction in DIRECTIONS: 
                positions[direction] += curr_waypoint[direction] * units

    result2 = abs(positions['N'] - positions['S']) + abs(positions['E'] - positions['W'])
    return result2


if __name__ == "__main__":
    file = 'input/day12.txt'
    data = read_input(file)
    result1 = solve(data, 'E')
    result2 = solve2(data, collections.defaultdict(int, {'N': 1, 'E': 10}))
    print(f"Result for part 1: {result1}\nResult for part 2: {result2}")