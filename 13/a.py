#!/usr/bin/python3

import io
import numpy as np
import sys
import re

inp = sys.stdin.read()
inp_first, inp_second = inp.split('\n\n')

dot_ixs = np.loadtxt(io.StringIO(inp_first), delimiter=',', dtype=int)
dot_ixs = dot_ixs[:, ::-1]

max_y, max_x = np.amax(dot_ixs, axis=0)

dots = np.zeros((max_y + 1, max_x + 1), dtype=int)
dots[dot_ixs[:, 0], dot_ixs[:, 1]] = 1

folds = [re.findall(r'(\w+)=(\w+)', l)[0] for l in inp_second.split('\n') if l]

for ax, pos in folds:
    pos = int(pos)
    dim = 0 if ax == 'y' else 1

    old_size = dots.shape
    assert pos == old_size[dim] // 2 # This makes it a lot easier...

    dot_ixs[:, dim] = np.minimum(dot_ixs[:, dim], 2 * pos - dot_ixs[:, dim])

    new_size = np.array(old_size)
    new_size[dim] = pos

    dots = np.zeros(new_size, dtype=int)
    dots[dot_ixs[:, 0], dot_ixs[:, 1]] = 1

    break

print(np.sum(dots))
