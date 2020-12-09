import itertools

def read_input(file):
    with open(file) as f: 
        data = [int(x) for x in f.read().splitlines()]
    return data

def find_number(numbers, offset):
    result1 = None
    result2 = None

    for idx, number in enumerate(numbers[offset:], offset): 
        combinations = itertools.combinations(numbers[idx-offset:idx], r=2)
        if any(sum(combi) == number for combi in combinations): 
                continue
        else: 
            result1 = number
            break

    for start in range(len(numbers)):
        for end in range(start+2, len(numbers)):
            sub_range = numbers[start:end]
            if sum(sub_range) == result1: 
                result2 = min(sub_range) + max(sub_range)
                return result1, result2
            if sum(sub_range) > result1: 
                break

    return result1, result2

if __name__ == "__main__":
    file = 'input/day09.txt'
    data = read_input(file)
    result1, result2 = find_number(data, 25)
    print(f"Result for part 1: {result1}\nResult for part 2: {result2}")