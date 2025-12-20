import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import run_solution

def parse(raw_data):
    grid = []
    operators = []
    for line in raw_data:
        line = line.strip()
        if not line:
            continue        
        tokens = line.split()
        try:
            row = [int(x) for x in tokens]
            grid.append(row)
        except ValueError:
            operators.extend(tokens)
            
    return grid, operators

def get_columns(data):
    columns = [[data[0][r][c] for r in range(len(data[0]))] for c in range(len(data[0][0]))]
    return columns

def part1(data):
    columns = get_columns(data)
    results = []
    for x, column in enumerate(columns):
        print(column)
        operator = data[1][x]
        result = 0
        for i, val in enumerate(column):
            if result == 0:
                result = val
            if (i + 1) < len(column):
                next_val = column[i + 1]
                if operator == "*":
                    result *= next_val
                elif operator == "+":
                    result += next_val
                elif operator == "-":
                    result -= next_val
                elif operator == "/":
                    result /= next_val
        results.append(result)
    return sum(results)
        
def part2(data):
    operators = data[1]
    columns = get_columns(data)
    results = []
    for x, column in enumerate(columns):
        print(column)
        operator = operators[x]
        max_num_length = len(str(max(column)))
        for val in range(max_num_length, 0, -1):
            new_num = "0"
            for i, num in enumerate(column):
                num_filed = str(num).zfill(max_num_length)
                value = ""
                try:
                    value = num_filed[val - 1]
                except IndexError:
                    value = ""
                new_num += value
            print(int(new_num))
    return ""
                    

if __name__ == "__main__":
    is_test = False
    if (sys.argv and len(sys.argv) > 1 and sys.argv[1] == "-t"):
        is_test = True
    run_solution(__file__, parse, part1, part2, is_test)
