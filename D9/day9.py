import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import run_solution

def parse(raw_data):
    return [(int(p.split(',')[0]), int(p.split(',')[1])) for p in [d.replace('\n', '') for d in raw_data]]

def part1(data):
    biggest_area = 0
    for point in data:
        x, y = point
        for other_point in data:
            if other_point == point:
                continue
            ox, oy = other_point
            area = max(1, abs(ox - x - 1)) * max(1, abs(oy - y - 1))
            if area > biggest_area:
                biggest_area = area
    return biggest_area


def part2(data):
    return "TODO"

if __name__ == "__main__":
    is_test = False
    print(sys.argv)
    if (sys.argv and len(sys.argv) > 1 and sys.argv[1] == "t"):
        is_test = True
    run_solution(__file__, parse, part1, part2, is_test)
