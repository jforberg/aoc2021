#!/usr/bin/python3

import numpy as np
import sys

data = np.loadtxt(sys.stdin, delimiter=',', dtype=int)

max_pos, min_pos = np.amax(data), np.amin(data)

# List of possible target positions
pos_list = np.r_[min_pos:max_pos + 1]

# On axis 0: the crabs. On axis 1, the target positions. Values: the distance crab needs to move to
# get to that position.
distances = pos_list - data[:, np.newaxis]

# Cost for each crab to move to each position
cost_distr = (np.abs(distances) + np.square(distances)) // 2

best_pos = np.argmin(np.sum(cost_distr, axis=0))

total_cost = np.sum(cost_distr[:, best_pos])
print(total_cost)
