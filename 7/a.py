#!/usr/bin/python3

import numpy as np
import sys

data = np.loadtxt(sys.stdin, delimiter=',')
pos = np.median(data)
cost = np.sum(np.abs(data - pos))
print(int(cost))
