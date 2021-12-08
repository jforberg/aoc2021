#!/usr/bin/python3

import numpy as np
import sys

inp = sys.stdin.read().replace('|', '')

lines = inp.split('\n')
if not lines[-1]:
    lines.pop()

def parse_line(line, pattern, challenge):
    for j, word in enumerate(line.split()):
        for char in word:
            c = ord(char) - ord('a')

            if j < 10:
                pattern[c, j] = 1
            else:
                challenge[c, j - 10] = 1

reference = np.reshape([
#   a  b  c  d  e  f  g
    1, 1, 1, 0, 1, 1, 1, # 0
    0, 0, 1, 0, 0, 1, 0, # 1
    1, 0, 1, 1, 1, 0, 1, # 2
    1, 0, 1, 1, 0, 1, 1, # 3
    0, 1, 1, 1, 0, 1, 0, # 4
    1, 1, 0, 1, 0, 1, 1, # 5
    1, 1, 0, 1, 1, 1, 1, # 6
    1, 0, 1, 0, 0, 1, 0, # 7
    1, 1, 1, 1, 1, 1, 1, # 8
    1, 1, 1, 1, 0, 1, 1, # 9
    ], (10, 7)).astype(bool).T

print(np.sum(reference, axis=1))

for problem_idx, line in enumerate(lines):
    pattern = np.zeros((7, 10), dtype=bool)
    challenge = np.zeros((7, 4), dtype=bool)
    parse_line(line, pattern, challenge)
    mapping = np.zeros((7, 7), dtype=bool)

    seg_sums = np.sum(pattern, axis=1)
    print(seg_sums)

    # Some are easy to find just by looking at the column sums
    b_idx = np.argmax(seg_sums == 6)
    e_idx = np.argmax(seg_sums == 4)
    f_idx = np.argmax(seg_sums == 9)


    print((b_idx, e_idx, f_idx))

    # a and c
