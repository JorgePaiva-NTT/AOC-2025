import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import run_solution

def parse(raw_data):
    return raw_data.splitlines()

def part1(data):
    return "TODO"

if __name__ == "__main__":
    run_solution(__file__, parse, part1, part2)
