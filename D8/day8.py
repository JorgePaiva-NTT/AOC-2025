import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import run_solution

def parse(raw_data):
    return raw_data.splitlines()

def part1(data):
    return "TODO"

def part2(data):
    return "TODO"

if __name__ == "__main__":
    is_test = False
    print(sys.argv)
    if (sys.argv and len(sys.argv) > 1 and sys.argv[1] == "t"):
        is_test = True
    run_solution(__file__, parse, part1, part2, is_test)
