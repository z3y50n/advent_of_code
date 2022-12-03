import string

def read_data(filename):
    with open(filename, "r") as f:
        data = f.read().strip().split("\n")
    return data

t_data = read_data("test_input.txt")
data = read_data("input.txt")

priorities = {x: i+1 for i, x in enumerate(string.ascii_letters)}

def part1(data):
    s = 0
    for rucksack in data:
        first = set(rucksack[:len(rucksack) // 2])
        second = set(rucksack[len(rucksack) // 2:])
        duplicate = first.intersection(second).pop()
        s += priorities[duplicate]
    return s

assert part1(t_data) == 157
print(part1(data))

def part2(data):
    s = 0
    for i in range(0, len(data), 3):
        first = set(data[i])
        second = set(data[i+1])
        third = set(data[i+2])
        common = first.intersection(second).intersection(third).pop()
        s += priorities[common]
    return s

assert part2(t_data) == 70
print(part2(data))