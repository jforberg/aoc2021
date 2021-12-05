#!/usr/bin/python3

import io
import numpy as np
import sys

preproc = sys.stdin.read().replace('->', ',')

data = np.genfromtxt(io.StringIO(preproc), dtype=int, delimiter=',')

max_x = np.amax(data[:, [0, 2]])
max_y = np.amax(data[:, [1, 3]])

density = np.zeros((max_x + 1, max_y + 1), dtype=int)

def diag(x1, x2, y1, y2):
    ixs = ([], [])
    x, y = x1, y1
    ixs[1].append(x)
    ixs[0].append(y)

    while x != x2 or y != y2:
        x += np.sign(x2 - x)
        y += np.sign(y2 - y)
        ixs[1].append(x)
        ixs[0].append(y)

    return ixs

for (x1, y1, x2, y2) in data:
    if x1 != x2 and y1 != y2:
        ixs = diag(x1, x2, y1, y2)
        density[ixs] += 1
    else:
        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1
        density[y1:y2 + 1, x1:x2 + 1] += 1

print(np.count_nonzero(density >= 2))
