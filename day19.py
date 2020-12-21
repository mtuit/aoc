import collections
import copy
import itertools
import re

def read_input(file):
    with open(file) as f: 
        data = f.read().split('\n\n')
    return data


def parse_rules(rules):
    result = collections.defaultdict(list)

    for rule in rules: 
        rule_split = rule.split(': ')
        rule_number = int(rule_split[0])
        rule_contents = rule_split[1].split(' | ')
 
        for rule_content in rule_contents: 
            if rule_content in ['"b"', '"a"']: 
                result[rule_number].append(rule_content.replace('"', ''))
            else:
                rule_content = rule_content.split(' ')
                rule_content = [int(n) for n in rule_content]
                result[rule_number].append(rule_content)

    return result


def gen_regex(rules, key, part2=False): 
    if part2: 
        if key == 8: 
            return gen_regex(rules, 42, True) + '+'
        elif key == 11: 
            a = gen_regex(rules, 42, True)
            b = gen_regex(rules, 31, True)
            return '(?:' + '|'.join(f'{a}{{{n}}}{b}{{{n}}}' for n in range(1, 10)) + ')'
    
    rule = rules[key]
    if rule in [['a'], ['b']]:
        return rule[0]
    else: 
        result = []
        for part in rule: 
            if part2: 
                result.append(''.join(gen_regex(rules, number, True) for number in part))
            else: 
                result.append(''.join(gen_regex(rules, number) for number in part))
        return '(?:' + '|'.join(result) + ')'
            

def solve(rules, msgs):
    rules = parse_rules(rules)
    reg, reg2 = gen_regex(rules, 0), gen_regex(rules, 0, True)

    matches, matches2 = [], [] 
    for msg in msgs: 
        matches.append(bool(re.fullmatch(reg, msg)))
        matches2.append(bool(re.fullmatch(reg2, msg)))

    return matches.count(True), matches2.count(True)


if __name__ == "__main__":
    file = 'input/day19.txt'
    data = read_input(file)
    rules, msgs = data[0].split('\n'), data[1].split('\n')
    result1, result2 = solve(rules, msgs)
    print(f"Result for part 1: {result1}\nResult for part 2: {result2}")