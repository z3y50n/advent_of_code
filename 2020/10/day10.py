def read_data(filename):
    with open(filename, "r") as f:
        data = f.read().split("\n")[:-1]
    return [int(jolt) for jolt in data]

jolts = read_data("day10.txt")

# PART 1
def part_1(jolts):
    diffs = {1:0, 2:0, 3:1}
    prev = 0
    for i in sorted(jolts):
        diffs[i-prev] += 1
        prev = i
    return diffs

diffs = part_1(jolts)
print(diffs[1] * diffs[3])

# PART 2
def part_2(jolts):
    jolts = sorted(jolts)
    counter = {0:1}
    for i in sorted(jolts):
        counter[i] = counter.get(i - 3, 0) + counter.get(i-2, 0) + counter.get(i-1,0)
    return counter[jolts[-1]]

print(part_2(jolts))
