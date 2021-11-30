import numpy as np
import math 
import os
import itertools

# Load input
if os.path.exists('input/day01.txt'):
    data = np.loadtxt('input/day01.txt')
else: 
    print(f"Couldn't find input file! Make sure input file is downloaded and named: 'day01.txt'")
    exit()

def find_result(data, num_elements):
    return int(np.prod(list(filter(lambda x: sum(x) == 2020, itertools.combinations(data, num_elements)))))
    
# Solve part 1
result_part1 = find_result(data, 2)

# Solve part 2
result_part2 = find_result(data, 3)

# Print results
print(f"Result for part 1 is: {result_part1}\nResult for part 2 is: {result_part2}")