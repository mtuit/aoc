def read_input(file):
    with open(file) as f: 
        data = f.read().splitlines()
    return data


def process_data(data):
    result1 = None
    result2 = None

    return result1, result2



if __name__ == "__main__":
    file = 'input/day08.txt'
    data = read_input(file)
    result1, result2 = process_data(data)

    print(f"Result for part 1: {result1}\nResult for part 2: {result2}")