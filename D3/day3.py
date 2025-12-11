import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import run_solution

def parse(raw_data):
    return raw_data.splitlines()

def part1(data):
    total_joltage = 0
    for line in data:
        max_joltage = 0
        length = len(line)
        for i in range(length):
            for j in range(i + 1, length):
                joltage = int(line[i] + line[j])
                if joltage > max_joltage:
                    max_joltage = joltage
        total_joltage += max_joltage
    return total_joltage

# version 2 uses 12 digits per line
def part2(data):
    n = 12
    total = []
    for line in data:
        result = []
        start_pos = 0
        s = line
        for _ in range(n):
            can_skip = len(s) - start_pos - (n - len(result))
            search_segment = s[start_pos : start_pos + can_skip + 1]
            max_digit = max(search_segment)
            best_pos = start_pos + search_segment.index(max_digit)
            result.append(max_digit)
            start_pos = best_pos + 1
        total.append(int(''.join(result)))
    return sum(total)
        
if __name__ == "__main__":
    is_test = False
    print(sys.argv)
    if (sys.argv and len(sys.argv) > 1 and sys.argv[1] == "-t"):
        is_test = True
    run_solution(__file__, parse, part1, part2, is_test)
