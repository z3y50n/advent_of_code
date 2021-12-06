def read_data(filename):
    with open(filename, "r") as f:
        data = f.read().strip().split(",")
    return list(map(int, data))


t_fish = read_data("test_input.txt")
fish = read_data("input.txt")


# PART 1 (STUPID)
def part1(fish, days):
    p0 = len(fish)
    for day in range(days):
        new = fish.count(0)
        p = p0 + new
        for i, f in enumerate(fish):
            if f == 0:
                fish[i] = 6
            else:
                fish[i] -= 1
        if new != 0:
            fish.extend([8] * new)
        p0 = p
    return p


assert part1(t_fish.copy(), 80) == 5934
print(f"Part1: {part1(fish.copy(), 80)}")


# PART 2 (FAST)
def part2(fish, days):
    state = [fish.count(i) for i in range(9)]
    for day in range(days):
        new = state.pop(0)
        state[6] += new
        state.append(new)
    return sum(state)


assert part2(t_fish, 256) == 26984457539
print(part2(fish, 256))
