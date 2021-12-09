#!/usr/bin/python3

import numpy as np
import sys
import io

inp = sys.stdin.read()
w = len(inp.split('\n')[0])

data = np.genfromtxt(io.StringIO(inp), delimiter=w * [1], dtype=int)

visited = data == 9

def basin(i, j, r):
    if i < 0 or i >= data.shape[0] or j < 0 or j >= data.shape[1]:
        return 0

    if visited[i, j]:
        return 0

    d = data[i, j]

    if d <= r:
        return 0

    visited[i, j] = 1

    return (
        1 +
        basin(i + 1, j, d) +
        basin(i - 1, j, d) +
        basin(i, j + 1, d) +
        basin(i, j - 1, d)
    )

sizes = []

for i, j in sorted(np.ndindex(data.shape), key=lambda x: data[x[0], x[1]]):
    s = basin(i, j, -1)
    if s:
        sizes.append(s)

print(np.product(sorted(sizes)[-3:]))
