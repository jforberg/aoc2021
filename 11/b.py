#!/usr/bin/python3

import numpy as np
import sys
import io

inp = sys.stdin.read()
w = len(inp.split('\n')[0])

data = np.genfromtxt(io.StringIO(inp), delimiter=w * [1], dtype=int)

def shift_xy(a, dx, dy):
    s = np.roll(a, (dx, dy), axis=(1, 0))

    if dy >= 0:
        s[:dy, :] = 0
    else:
        s[dy:, :] = 0

    if dx >= 0:
        s[:, :dx] = 0
    else:
        s[:, dx:] = 0

    return s

def adjacent(a):
    weight = (
        shift_xy(a, -1, 0) + # NN
        shift_xy(a, -1, 1) + # NE
        shift_xy(a, 0, 1) +  # EE
        shift_xy(a, 1, 1) +  # SE
        shift_xy(a, 1, 0) +  # SS
        shift_xy(a, 1, -1) + # SW
        shift_xy(a, 0, -1) + # WW
        shift_xy(a, -1, -1)  # NW
    )
    return weight

def step():
    global data, flash_count

    flashed = np.zeros_like(data)
    data += 1

    while True:
        flash = ((data > 9) * (1 - flashed)).astype(int)

        if not np.any(flash):
            break

        flashed = np.maximum(flashed, flash)

        adjustment = adjacent(flash)
        data += adjustment

    data[np.nonzero(flashed)] = 0
    return np.count_nonzero(flashed)

i = 0
while True:
    i += 1
    if step() == np.size(data):
        break

print(i)
