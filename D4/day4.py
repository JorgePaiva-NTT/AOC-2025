import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import run_solution

def parse(raw_data):
    return raw_data

def part1(data):
    data = [line.replace("\n", "") for line in data]
    coordinates = []
    for x in range(len(data)):
        for y in range(len(data[x])):
            current_char = data[x][y]
            if current_char == ".":
                continue
            else:
                counter = check_adjacent(data, x, y)
                if (counter < 4):
                    coordinates.append((x, y))
    return len(coordinates)
        
def part2(data):
    data = [line.replace("\n", "") for line in data]
    coordinates = []
    found_any = False
    while True:
        counter = 0
        found_any = False
        for x in range(len(data)):
            for y in range(len(data[x])):
                if (x, y) in coordinates:
                    continue
                current_char = data[x][y]
                if current_char == ".":
                    continue
                else:
                    counter = check_adjacent(data, x, y)
                    if (counter < 4):
                        found_any = True
                        coordinates.append((x, y))
        if not found_any:
            break
        for coord in coordinates:
            x, y = coord
            data[x] = data[x][:y] + "." + data[x][y+1:]
    return len(coordinates)
            

def check_adjacent(data, x, y):
    count = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if nx >= 0 and nx < len(data) and ny >= 0 and ny < len(data[x]):
                adjacent_char = data[nx][ny]
                if (adjacent_char == "@"):
                    count += 1
    return count

if __name__ == "__main__":
    is_test = False
    if (sys.argv and len(sys.argv) > 1 and sys.argv[1] == "-t"):
        is_test = True
    run_solution(__file__, parse, part1, part2, is_test)
