

def read_input(file):
    with open(file) as f: 
        data = f.read().splitlines()
    return data


def check_valid_passwords(data):
    valid_count_passwords = 0
    valid_position_passwords = 0

    for password in data: 

        password_split = password.replace(':', '').split(' ')
        minimum, maximum = [int(number) for number in password_split[0].split('-')]
        character = password_split[1]
        password = password_split[2]

        if minimum <= password.count(character) <= maximum:
            valid_count_passwords += 1

        first_check = password[minimum - 1] == character
        second_check = password[maximum - 1] == character

        if first_check ^ second_check:
            valid_position_passwords += 1

    return valid_count_passwords, valid_position_passwords
        

if __name__ == "__main__":
    file = 'input/day02.txt'
    data = read_input(file)
    result_part1, result_part2 = check_valid_passwords(data)
    print(f"Result for part 1: {result_part1}\nResult for part 2: {result_part2}")