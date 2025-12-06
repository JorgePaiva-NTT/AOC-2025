import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import run_solution

def parse(raw_data):
    return raw_data.split(',')

def part1(data):
    findings = []
    for value_range in data:
        start = int(value_range.split('-')[0])
        end = int(value_range.split('-')[1])
        for num in range(start, end + 1):
            num_of_digits = len(str(num))
            if (num_of_digits % 2 != 0):
                continue
            str_num = str(num)
            left = str_num[0:num_of_digits//2]
            right = str_num[num_of_digits//2:num_of_digits]
            if (left == right):
                findings.append(num)
    return str(sum(findings))
            

if __name__ == "__main__":
    run_solution(__file__, parse, part1)
