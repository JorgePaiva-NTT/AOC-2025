import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import run_solution

def parse(raw_data):
    return [list(line.strip()) for line in raw_data]

def part1(data):
    scoord = None
    hatCoords = []
    beams = []
    counter = [0]
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            if char == 'S':
                scoord = (i, j)
            if char == '^':
                hatCoords.append((i, j))
    beams = []
    paths = []
    hitted = []
    beams.append([1, scoord[1]])
    counter[0] = 0
    stepBeamDown(beams[0], hatCoords, counter, paths, data, hitted)
    return counter[0]
    
def stepBeamDown(beam, hats, counter, paths, data, hitted):
    if (beam[0] >= len(data)):
        return
    
    paths.append(beam.copy())
    if (beam[0], beam[1]) not in hats:
        beam[0] += 1
        stepBeamDown(beam, hats, counter, paths, data, hitted)
        
    else:
        if (beam[0], beam[1]) in hitted:
            return
        counter[0] += 1
        hitted.append((beam[0], beam[1]))
        splitl = [beam[0], beam[1]-1]
        if (splitl[1] >= 0 and splitl not in paths):
            stepBeamDown(splitl, hats, counter, paths, data, hitted)
        
        splitr = [beam[0], beam[1]+1]
        if (splitr[1] < len(data[0]) and splitr not in paths):
            stepBeamDown(splitr, hats, counter, paths, data, hitted)
            
        return
     
def print_paths(paths, data):
    return
    for p in paths:
        if (p[0] >= len(data)):
            continue
        if data[p[0]][p[1]] == '^':
            continue
        data[p[0]][p[1]] = '|'
    for line in data:
        print(line)     

def part2(data):
    return "TODO"

if __name__ == "__main__":
    is_test = False
    print(sys.argv)
    if (sys.argv and len(sys.argv) > 1 and sys.argv[1] == "t"):
        is_test = True
    run_solution(__file__, parse, part1, part2, is_test)
