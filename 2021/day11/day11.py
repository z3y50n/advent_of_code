import numpy as np


def read_data(filename):
    with open(filename, "r") as f:
        data = f.read().strip().split("\n")
    data = [list(row) for row in data]
    return np.asarray(data, dtype=int)


t_data = read_data("test_input.txt")
data = read_data("input.txt")
STEPS = 100

# Try to remove some for loops?
def round(data):
    data += 1
    while np.sum(data >= 10):  # While there are flashes
        # Loop through each octopus
        for i, row in enumerate(data):
            for j, col in enumerate(row):
                if col < 10:
                    continue
                # If octopus will flash
                # make zero
                data[i, j] = 0
                # all neighbours should be +1
                i_start = i - 1 if i > 0 else i
                i_end = i + 1 if i < data.shape[0] - 1 else i
                j_start = j - 1 if j > 0 else 0
                j_end = j + 1 if j < data.shape[1] - 1 else j
                for k in range(i_start, i_end + 1):
                    for l in range(j_start, j_end + 1):
                        if data[k, l] != 0:
                            data[k, l] += 1


# PART 1
def part1(data, steps):
    flashes = 0
    for step in range(steps):
        round(data)
        flashes += np.sum(data == 0)
    return flashes


assert part1(t_data.copy(), STEPS) == 1656
print(part1(data.copy(), STEPS))


def part2(data):
    step = 0
    while not np.all(data == 0):
        round(data)
        step += 1
    return step


assert part2(t_data) == 195
print(part2(data))
