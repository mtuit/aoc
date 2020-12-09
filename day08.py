import collections
import copy

def read_input(file):
    with open(file) as f: 
        data = f.read().splitlines()
    return data


def run_instructions(instructions, full_terminate=False):
    visited = set()
    curr_instruction = 0
    acc = 0
    
    while curr_instruction < len(instructions):
        if curr_instruction in visited: 
            if full_terminate: 
                return None
            elif not full_terminate: 
                return acc

        instr_type, value = instructions[curr_instruction].split(' ')
        visited.add(curr_instruction)

        if instr_type == 'acc':
            acc += int(value)
            curr_instruction += 1
        elif instr_type == 'nop': 
            curr_instruction += 1
        elif instr_type == 'jmp': 
            curr_instruction += int(value)

    return acc


def full_terminate(instructions):
    acc = None
    for idx, instruction in enumerate(instructions): 
        instr_type, value = instruction.split(' ')
        if instr_type == 'acc': 
            continue
    
        if instr_type == 'jmp':
            new_instruction = instruction.replace('jmp', 'nop')
        elif instr_type == 'nop':
            new_instruction = instruction.replace('nop', 'jmp')

        new_instructions = copy.deepcopy(instructions)
        new_instructions[idx] = new_instruction
        acc = run_instructions(new_instructions, full_terminate=True)

        if acc is not None: 
            return acc

    return acc


if __name__ == "__main__":
    file = 'input/day08.txt'
    data = read_input(file)
    result1 = run_instructions(data, full_terminate=False)
    result2 = full_terminate(data)

    print(f"Result for part 1: {result1}\nResult for part 2: {result2}")
