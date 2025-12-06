import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import run_solution

def parse(raw_data):
    return raw_data.splitlines()

def part1(data):
    counter = 0
    value = 50
    for line in data:
        direction = line[0]
        amount = int(line[1:])
        if (direction == 'L'):
            value -= amount
            if (value <= 0):
                value = 100 - abs(value) 
                if (value == 100):
                    value = 0
        elif (direction == 'R'):
            value += amount
            if (value >= 100):
                value = value - 100
        if (value == 0):
            counter += 1
    solution = str(counter)
    return solution

if __name__ == "__main__":
    run_solution(__file__, parse, part1)
