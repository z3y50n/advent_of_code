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

# PART 1
def part1(data):
    inc = sum(1 for i in range(1, len(data)) if data[i] > data[i - 1])
    return inc


assert part1(t_data) == 7
print(part1(data))

# PART 2
def part2(data):
    inc = sum(data[i+3] > data[i] for i in range(0, len(data)-3))
    return inc


assert part2(t_data) == 5
print(part2(data))
