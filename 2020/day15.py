import collections
import copy
import itertools


def solve(data):
    turns = {number: idx+1 for idx, number in enumerate(data)}
    last_number = data[-1]
    print(turns)
    for turn in range(len(data), 30000000):
        turns[last_number], last_number = turn, turn - turns.get(last_number, turn)

        if turn == 2019: 
            print(f"Result for part 1: {last_number}")
           
    print(f"Result for part 2: {last_number}")
    

if __name__ == "__main__":
    file = 'input/day15.txt'
    data = [2,1,10,11,0,6]
    solve(data)