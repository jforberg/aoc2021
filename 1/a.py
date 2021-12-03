#!/usr/bin/python3

import numpy as np
import sys

data = np.loadtxt(sys.stdin)

answer = np.count_nonzero(np.diff(data) > 0)
print(answer)
