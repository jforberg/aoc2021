#!/usr/bin/python3

import numpy as np
import os
from scipy import stats

my_dir = os.path.dirname(os.path.realpath(__file__))

data = np.genfromtxt('%s/input.txt' % my_dir, dtype=int, delimiter=12*[1])
mode, counts = stats.mode(data, axis=0)

def from_bits(bs):
    return int(''.join(map(str, bs)), 2)

gamma = from_bits(mode[0, :])
epsilon = from_bits(1 - mode[0, :])

power = gamma * epsilon
print(power)
