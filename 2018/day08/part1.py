#!/usr/bin/env python3


def parse(data):
    n_children, n_meta = data[:2]
    data = data[2:]
    total = 0

    for i in range(n_children):
        data, sub_score = parse(data)
        total += sub_score

    total += sum(data[:n_meta])
    return data[n_meta:], total


data = [int(x) for x in open('input.txt').read().strip().split()]
print(parse(data)[1])
