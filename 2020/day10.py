import itertools
import collections

def read_input(file):
    return list(map(int, open(file)))
            
            
def solve(data):
    result1, result2 = (None, None)
    jolts1, jolts3 = ([1], [1])
    data.sort()

    for i in range(len(data)-1): 
        if (data[i] + 1) == data[i+1]: 
            jolts1.append(1)
        elif data[i] + 3 == data[i+1]: 
            jolts3.append(1)

    result1 = len(jolts1) * len(jolts3)

    possibilities = collections.defaultdict(int)
    possibilities[0] = 1
    for number in data: 
        possibilities[number] = possibilities[number-1] + possibilities[number-2] + possibilities[number-3]
    
    result2 = possibilities[max(data)]
    return result1, result2

if __name__ == "__main__":
    file = 'input/day10.txt'
    data = read_input(file)
    result1, result2 = solve(data)
    print(f"Result for part 1: {result1}\nResult for part 2: {result2}")