#!/usr/bin/env python3

import re
from collections import Counter


def minutes_per_guard():
    data = sorted(open('input.txt').read().splitlines())

    mpg = dict()              # k=guard_id, v=[all minutes asleep]
    current_guard = None
    start = None
    r_cycle = lambda s: rf".*:(\d\d).*{s}"  # falls or wakes

    for line in data:
        guard = re.findall(r".*#(\d+).*", line)
        if guard:
            current_guard = int(guard[0])

        falls = re.findall(r_cycle('falls'), line)
        if falls:
            start = int(falls[0])

        wakes = re.findall(r_cycle('wakes'), line)
        if wakes:
            finish = int(wakes[0])
            new_mins = list(range(start, finish))
            current_mins = mpg.get(current_guard, [])
            mpg[current_guard] = current_mins + new_mins

    return mpg


def part1(minutes_per_guard):
    # k = guard id, v = total number of minutes asleep
    count_per_guard = {k: len(v) for (k, v) in minutes_per_guard.items()}
    # sleeper with max number of minutes asleep
    sleeper_id = max(count_per_guard, key=count_per_guard.get)
    # k = minute, v = how many times
    frequencies = Counter(minutes_per_guard[sleeper_id])
    # minute where guard was mostly asleep
    minute = max(frequencies, key=frequencies.get)

    return sleeper_id * minute


def part2(minutes_per_guard):
    # eg: {10: (24, 2), 99: (45, 3)}
    most_commons = {k: Counter(v).most_common(1)[0] for (k, v) in minutes_per_guard.items()}
    # eg: 99 (because 45 appears 3 times)
    sleeper_id = max(most_commons, key=lambda k: most_commons[k][1])
    # eg: 45
    minute = most_commons[sleeper_id][0]

    return sleeper_id * minute


mpg = minutes_per_guard()
print(part1(mpg))
print(part2(mpg))
