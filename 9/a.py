#!/usr/bin/python3

import numpy as np
import sys
import io

inp = sys.stdin.read()
w = len(inp.split('\n')[0])

data = np.genfromtxt(io.StringIO(inp), delimiter=w * [1], dtype=int)

def shift(arr, d, axis):
    s = np.roll(arr, d, axis=axis)
    if d > 0:
        np.moveaxis(s, axis, 0)[:d] = np.moveaxis(arr, axis, 0)[1]
    else:
        np.moveaxis(s, axis, 0)[d:] = np.moveaxis(arr, axis, 0)[-2]
    return s

cond = (
    (data < shift(data, 1, 0)) *
    (data < shift(data, -1, 0)) *
    (data < shift(data, 1, 1)) *
    (data < shift(data, -1, 1))
)

risk = (1 + data) * cond

print(np.sum(risk))
