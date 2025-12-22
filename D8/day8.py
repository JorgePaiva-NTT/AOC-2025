import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import run_solution
from collections import defaultdict

import math

class JunctionBox:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def dist(self, p2: "JunctionBox"):
        return math.sqrt(math.pow(p2.x - self.x, 2) + math.pow(p2.y - self.y, 2) + math.pow(p2.z - self.z, 2))

def parse(raw_data):
    d = [d.replace("\n", "") for d in raw_data]
    positions: list[JunctionBox] = []
    for i, line in enumerate(d):
        parts = line.split(",")
        positions.append(JunctionBox(int(parts[0]), int(parts[1]), int(parts[2])))
    return positions

def find(UF, x):
    if x==UF[x]:
        return x
    UF[x] = find(UF, UF[x])
    return UF[x]

def mix(UF, x, y):
    UF[find(UF, x)] = find(UF, y)

def part1(data):
    D = []
    for i, jb1 in enumerate(data):
        for j, jb2 in enumerate(data):
            distance = jb1.dist(jb2)
            if i > j:
                D.append((distance, i, j))
    UF = {i: i for i in range(len(data))}
    D = sorted(D)
    for _, i, j in D[:1000]:
        mix(UF, i, j)
    
    SZ = defaultdict(int)
    for x in range(len(data)):
        SZ[find(UF, x)] += 1
    S = sorted(SZ.values())
    return (S[-1] * S[-2] * S[-3])

def part2(data):
    D = []
    for i, jb1 in enumerate(data):
        for j, jb2 in enumerate(data):
            distance = jb1.dist(jb2)
            if i > j:
                D.append((distance, i, j))
    D = sorted(D)

    UF = {i: i for i in range(len(data))}
    for _, i, j in D[:1000]:
        mix(UF, i, j)

    connections = 0
    result = 0
    for (d, i, j) in D:
        if find(UF, i) != find(UF, j):
            connections += 1
            mix(UF, i, j)
    result = data[i].x * data[j].x
    return result


if __name__ == "__main__":
    is_test = False
    print(sys.argv)
    if (sys.argv and len(sys.argv) > 1 and sys.argv[1] == "t"):
        is_test = True
    run_solution(__file__, parse, part1, part2, is_test)
