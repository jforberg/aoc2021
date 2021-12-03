#!/usr/bin/python3

import numpy as np
import sys

data = np.loadtxt(sys.stdin)

indices = np.arange(3)[np.newaxis, :] + np.arange(len(data) - 2)[:, np.newaxis]

sums = np.sum(data[indices], axis=1)

answer = np.count_nonzero(np.diff(sums) > 0)
print(answer)
