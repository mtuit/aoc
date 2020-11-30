import numpy as np
import math 
import os

# Load input
if os.path.exists('input/day01.txt'):
    data = np.loadtxt('input/day01.txt')
else: 
    print(f"Couldn't find input file! Make sure input file is downloaded and named: 'day01.txt'")
    exit()

# Solve part 1
result_part1 = None

# Solve part 2
result_part2 = None

# Print results
print(f"Result for part 1 is: {result_part1}\nResult for part 2 is: {result_part2}")
