import re

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def read_input(file):
    with open(file) as f: 
        data = [password.split() for password in f.read().split('\n\n')]
    return data

def count_valid_passwords(passwords):
    count_part1, count_part2 = 0, 0

    for password in passwords: 
        password = {k:v for k, v in (field.split(':') for field in password)}

        if all(key in password for key in fields):
            count_part1 += 1

            if 1920 <= int(password['byr']) <= 2002 \
                    and 2010 <= int(password['iyr']) <= 2020 \
                    and 2020 <= int(password['eyr']) <= 2030 \
                    and (password['hgt'][-2:] == 'cm' and 150 <= int(password['hgt'][:-2]) <= 193) \
                        ^ (password['hgt'][-2:] == 'in' and 59 <= int(password['hgt'][:-2]) <= 76) \
                    and re.fullmatch(r'#[0-9a-f]{6}', password['hcl']) \
                    and re.fullmatch(r'amb|blu|brn|gry|grn|hzl|oth', password['ecl']) \
                    and re.fullmatch(r'0*\d{9}', password['pid']): 
                count_part2 += 1

    return count_part1, count_part2

if __name__ == "__main__":
    file = 'input/day04.txt'
    data = read_input(file)
    result1, result2 = count_valid_passwords(data)
    print(f"Result for part 1: {result1}\nResult for part 2: {result2}")