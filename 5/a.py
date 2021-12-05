#!/usr/bin/python3

import io
import numpy as np
import sys

preproc = sys.stdin.read().replace('->', ',')

data = np.genfromtxt(io.StringIO(preproc), dtype=int, delimiter=',')

max_x = np.amax(data[:, [0, 2]])
max_y = np.amax(data[:, [1, 3]])

density = np.zeros((max_x + 1, max_y + 1), dtype=int)

for (x1, y1, x2, y2) in data:
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1

    assert x1 <= x2 and y1 <= y2

    if x1 != x2 and y1 != y2:
        continue

    density[y1:y2 + 1, x1:x2 + 1] += 1

print(np.count_nonzero(density >= 2))
