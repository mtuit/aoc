def read_input(file):
    with open(file) as f: 
        data = [x for x in f.read().strip().split('\n\n')]
    return data

def check_forms(data):
    count = 0
    count2 = 0

    for form in data: 
        count += len(set(form.replace('\n', '')))
        count2 += len(set.intersection(*map(set, form.split('\n'))))

    return count, count2

if __name__ == "__main__":
    file = 'input/day06.txt'
    data = read_input(file)
    result1, result2 = check_forms(data)
    print(f"Result for part 1: {result1}\nResult for part 2: {result2}")