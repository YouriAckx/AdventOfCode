#!/usr/bin/env python3

import re
from collections import Counter


def distance(c1, c2):
    return abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])


data = open('input.txt').read().splitlines()
coord = [(x, y) for (x, y) in (map(int, re.findall(r"\d+", line)) for line in data)]

# Find the perimeter
left = min(n[0] for n in coord)
right = max(n[0] for n in coord)
top = min(n[1] for n in coord)
bottom = max(n[1] for n in coord)

grid = {}   # k=point, v=index in coord (=location)

# Iterate over all points inside the perimeter +1 (to detect infinite areas)
for x in range(left-1, right+2):
    for y in range(top-1, bottom+2):
        p = (x, y)
        distances = [distance(p, c) for c in coord]
        lowest = min(distances)
        grid[p] = distances.index(lowest) if distances.count(lowest) == 1 else -1

# Any location found in the outer edge is an infinite area
edges = [
        [(x, top-1) for x in range(left-1, right+1)] +
        [(x, bottom+1) for x in range(left-1, right+1)] +
        [(left-1, y) for y in range(top-1, bottom+1)] +
        [(right+1, y) for y in range(top-1, bottom+1)]
    ]
edges = [item for sublist in edges for item in sublist]
infinites = {grid[p] for p in edges if grid[p] is not -1}

# For each location (key), count how many points are closest (value)
frequencies = Counter([v for v in grid.values() if v is not -1 and v not in infinites])

# Size of the largest finite area
print(max([f for f in frequencies.values()]))
