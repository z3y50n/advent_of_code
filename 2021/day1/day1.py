def read_data(filename):
    with open(filename, "r") as fp:
        data = fp.read().strip().split("\n")
    return list(map(int, data))


t_data = [
    199,
    200,
    208,
    210,
    200,
    207,
    240,
    269,
    260,
    263,
]
data = read_data("day1a.txt")
print(len(data))

# PART 1
def part1(data):
    inc = sum(1 for i in range(1, len(data)) if data[i] > data[i - 1])
    return inc


assert part1(t_data) == 7
print(part1(data))

# PART 2
def part2(data):
    inc = 0
    for i in range(1, len(data) - 2):
        m1 = sum(data[i - 1 : i + 2])
        m2 = sum(data[i : i + 3])
        if m2 > m1:
            inc += 1
    return inc


assert part2(t_data) == 5
print(part2(data))
