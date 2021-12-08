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
    ], (10, 7)).astype(int)

total_sum = 0

for problem_idx, line in enumerate(lines):
    pattern = np.zeros((7, 10), dtype=int)
    challenge = np.zeros((7, 4), dtype=int)
    parse_line(line, pattern, challenge)
    mapping = np.zeros((7, 7), dtype=int)

    # Sum of digits a segment is observed in
    seg_sums = np.sum(pattern, axis=1)

    # Sum of segments in each observed digit
    dig_sums = np.sum(pattern, axis=0)

    # Some segments are easy to find just by looking at the column sums
    b_seg = np.argmax(seg_sums == 6)
    e_seg = np.argmax(seg_sums == 4)
    f_seg = np.argmax(seg_sums == 9)

    def elim(candidates, those_which_its_not):
        l = list(filter(lambda x: x not in those_which_its_not, candidates))
        assert len(l) == 1
        return l[0]

    # Now look for digit one, the only one with two segments: one c, the other f
    one_idx = np.argmax(dig_sums == 2)
    one_cand, = np.nonzero(pattern[:, one_idx])
    c_seg = elim(one_cand, [f_seg])

    # Now the same for digit seven, it gives us segment a
    seven_idx = np.argmax(dig_sums == 3)
    seven_cand, = np.nonzero(pattern[:, seven_idx])
    a_seg = elim(seven_cand, [c_seg, f_seg])

    # Now digit four, it gives us segment d
    four_idx = np.argmax(dig_sums == 4)
    four_cand, = np.nonzero(pattern[:, four_idx])
    d_seg = elim(four_cand, [b_seg, c_seg, f_seg])

    # g is the last one
    g_seg = elim(np.r_[0:7], [a_seg, b_seg, c_seg, d_seg, e_seg, f_seg])

    mapping[0, a_seg] = 1
    mapping[1, b_seg] = 1
    mapping[2, c_seg] = 1
    mapping[3, d_seg] = 1
    mapping[4, e_seg] = 1
    mapping[5, f_seg] = 1
    mapping[6, g_seg] = 1

    local_sum = 0
    base = 1

    for c in reversed(challenge.T):
        trans = mapping @ c

        for d in range(10):
            if np.all(trans[np.newaxis, :] == reference[d, :]):
                local_sum += base * d
                base *= 10

    total_sum += local_sum

print(total_sum)
