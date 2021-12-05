import numpy as np
from copy import deepcopy


def read_data(filename):
    with open(filename, "r") as f:
        data = f.read().strip().split("\n\n")
    numbers = list(map(int, data[0].split(",")))
    boards = []
    for board in data[1:]:
        rows = board.split("\n")
        b = np.asarray(
            [np.fromstring(row, dtype=int, count=5, sep=" ") for row in rows]
        )
        boards.append(b)
    return boards, numbers


t_boards, t_numbers = read_data("test_input.txt")
boards, numbers = read_data("input.txt")

def bingo(board, n):
    for row in board:
        if np.all(row == -1):
            return True
    return False

# PART 1
def part1(boards, numbers):
    for n in numbers:
        for board in boards:
            x, y = np.where(board==n)
            if x.size > 0 and y.size > 0:
                board[x[0], y[0]] = -1
            if bingo(board, n) or bingo(board.T, n):
                return np.sum(board[board != -1]) * n
# We need deepcopy to leave the boards unchanged
# but it doesn't affect part 2 since it continues
# from where it left
assert part1(t_boards, t_numbers) == 4512
print(part1(boards, numbers))

# PART 2
def part2(boards, numbers):
    found = []
    for n in numbers:
        for i, board in enumerate(boards):
            if i in found:
                continue
            x, y = np.where(board==n)
            if x.size > 0 and y.size > 0:
                board[x[0], y[0]] = -1
            if bingo(board, n) or bingo(board.T, n):
                if len(found) == len(boards) - 1:
                    return np.sum(board[board != -1]) * n
                found.append(i)

assert part2(t_boards, t_numbers) == 1924
print(part2(boards, numbers))
