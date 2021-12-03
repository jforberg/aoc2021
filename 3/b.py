#!/usr/bin/python3

import numpy as np
import os
from scipy import stats

d = 12

my_dir = os.path.dirname(os.path.realpath(__file__))

data = np.genfromtxt('%s/input.txt' % my_dir, dtype=int, delimiter=12*[1])

oxy_candidates = data
co2_candidates = data

for i in range(data.shape[1]):
    oxy_mode, oxy_counts = stats.mode(oxy_candidates[:, i])
    co2_mode, co2_counts = stats.mode(co2_candidates[:, i])

    oxy_bit = oxy_mode[0]
    co2_bit = 1 - co2_mode[0]

    if oxy_counts[0] == oxy_candidates.shape[0] // 2:
        oxy_bit = 1
    if co2_counts[0] == co2_candidates.shape[0] // 2:
        co2_bit = 0

    if oxy_candidates.shape[0] > 1:
        oxy_candidates = oxy_candidates[oxy_candidates[:, i] == oxy_bit, :]
    if co2_candidates.shape[0] > 1:
        co2_candidates = co2_candidates[co2_candidates[:, i] == co2_bit, :]

def from_bits(bs):
    return int(''.join(map(str, bs)), 2)

assert oxy_candidates.shape[0] == 1
assert co2_candidates.shape[0] == 1

print(from_bits(oxy_candidates[0, :]) * from_bits(co2_candidates[0, :]))


