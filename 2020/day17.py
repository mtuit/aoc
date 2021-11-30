import collections
import copy
import itertools
import numpy as np
import scipy.ndimage

def read_input(file):
    with open(file) as f: 
        data = np.array([list(row) for row in f.read().splitlines()])
        data = np.where(data == '#', 1, 0)
    return data


def solve(data, cycles, dims):
    state = np.array(data)
    new_dims = dims - state.ndim
    state = np.expand_dims(state, tuple(range(new_dims)))

    kernel = np.ones((3,) * dims)
    kernel[(1,) * dims] = 0

    for cycle in range(cycles): 
        state = np.pad(state, (1,))
        neighbours = scipy.ndimage.convolve(state, kernel, mode='constant')
        state = np.where((neighbours == 3) | (state & (neighbours == 2)), 1, 0)

    return np.sum(state)


if __name__ == "__main__":
    file = 'input/day17.txt'
    data = read_input(file)
    result1 = solve(data, 6, 3)
    result2 = solve(data, 6, 4)
    print(f"Result for part 1: {result1}\nResult for part 2: {result2}")