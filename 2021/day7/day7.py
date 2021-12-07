def read_file(filename):
    with open(filename, "r") as f:
        data = f.read().strip().split(",")
    return list(map(int, data))

t_positions = read_file("test_input.txt")
positions = read_file("input.txt")


# PART 1
def part1(positions):
    left = min(positions)
    right = max(positions)
    fuels = []
    for i in range(left, right+1):
        fuels.append(sum(abs(pos-i) for pos in positions))

    return min(fuels)

assert part1(t_positions) == 37
print(part1(positions))


# PART 2 Using Arithmetic Progression
def gauss(x):
    return x * (x+1) / 2

def part2(positions):
    left = min(positions)
    right = max(positions)
    fuels = []
    for i in range(left, right+1):
        fuel = 0
        for pos in positions:
            diff = abs(pos-i)
            fuel += gauss(diff)
        fuels.append(int(fuel))
    return min(fuels)

assert part2(t_positions) == 168
print(part2(positions))

