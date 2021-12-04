#!/usr/bin/python3

import io
import numpy as np
import sys

first_line = sys.stdin.readline()
numbers = np.loadtxt(io.StringIO(first_line), delimiter=',', dtype=int)

board_data = np.loadtxt(sys.stdin, dtype=int)
boards = np.reshape(board_data, (-1, 5, 5))
board_count = board_data.shape[0]

have_bingo = np.zeros(board_count, dtype=bool)
won_boards = 0

marks = np.zeros_like(boards)

def mark_all(n):
    global marks
    marks += boards == n

def find_bingo(b, m, n):
    col_sums = np.sum(m, axis=0)
    row_sums = np.sum(m, axis=1)

    if np.any(col_sums == 5) or np.any(row_sums == 5):
        unmarked_sum = np.sum(b * (1 - m))
        return unmarked_sum * n

    return None

for n in numbers:
    mark_all(n)

    for i in range(boards.shape[0]):
        if have_bingo[i]:
            continue

        bingo = find_bingo(boards[i, :, :], marks[i, :, :], n)
        if bingo:
            have_bingo[i] = True
            won_boards += 1

            if won_boards == board_count:
                break

    if won_boards == board_count:
        break

print(bingo)
