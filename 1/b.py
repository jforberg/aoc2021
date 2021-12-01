#!/usr/bin/python3

import numpy as np
import os

my_dir = os.path.dirname(os.path.realpath(__file__))

data = np.loadtxt('%s/input.txt' % my_dir)

indices = np.arange(3)[np.newaxis, :] + np.arange(len(data) - 2)[:, np.newaxis]

sums = np.sum(data[indices], axis=1)

answer = np.count_nonzero(np.diff(sums) > 0)
print(answer)
