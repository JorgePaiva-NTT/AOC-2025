import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import run_solution

def parse(raw_data):
    newline_index = raw_data.index("\n") if "\n" in raw_data else None
    first_section = [line.replace("\n", "") for line in raw_data[:newline_index]]
    second_section = [line.replace("\n", "") for line in raw_data[newline_index+1:]]
    return (first_section, second_section)

def part1(data):
    fresh_intervals = data[0]
    ingredients = data[1]
    counter = 0
    for ingredient in ingredients:
        ingredient = int(ingredient)
        for interval in fresh_intervals:
            start, end = map(int, interval.split("-"))
            if ingredient >= start and ingredient <= end:
                counter += 1
                break
    return counter
    
def part2(data):
    intervals = list(sorted(data[0], key=lambda x: int(x.split("-")[0])))
    intervals = [list(map(int, interval.split("-"))) for interval in intervals]
    counter = 0
    for interval in intervals:
        for other_interval in intervals:
            if interval[0] == other_interval[0] and interval[1] == other_interval[1]:
                continue
            if not (interval[1] < other_interval[0] or interval[0] > other_interval[1]):
                interval[0] = min(interval[0], other_interval[0])
                interval[1] = max(interval[1], other_interval[1])
                intervals.remove(other_interval)
                intervals.append(interval)
                
    intervals = list(set(tuple(interval) for interval in intervals))
    for interval in intervals:
        counter += interval[1] - interval[0] + 1
    return counter
        
if __name__ == "__main__":
    is_test = False
    if (sys.argv and len(sys.argv) > 1 and sys.argv[1] == "-t"):
        is_test = True
    run_solution(__file__, parse, part1, part2, is_test)
