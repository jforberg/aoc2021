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

count = 0

for problem_idx, line in enumerate(lines):
    pattern = np.zeros((7, 10), dtype=int)
    challenge = np.zeros((7, 4), dtype=int)
    parse_line(line, pattern, challenge)

    for d in challenge.T:
        if np.sum(d) in [2, 3, 4, 7]:
            count += 1

print(count)
