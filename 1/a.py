#!/usr/bin/python3

import numpy as np
import os

my_dir = os.path.dirname(os.path.realpath(__file__))

data = np.loadtxt('%s/input.txt' % my_dir)

answer = np.count_nonzero(np.diff(data) > 0)
print(answer)
