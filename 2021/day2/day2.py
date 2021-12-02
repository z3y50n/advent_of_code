def read_data(filename):
    with open(filename, "r") as fp:
        data = fp.read().strip().split("\n")
    course = [tuple(line.split()) for line in data]
    return course


course = read_data("day2.txt")
t_course = [
    ("forward", "5"),
    ("down", "5"),
    ("forward", "8"),
    ("up", "3"),
    ("down", "8"),
    ("forward", "2"),
]

# PART 1
def part1(course):
    pos = [0, 0]  # horizontal, depth
    for cmd in course:
        d = cmd[0]
        u = int(cmd[1])
        if d == "forward":
            pos[0] += u
        elif d == "down":
            pos[1] += u
        else:
            pos[1] -= u
    return pos[0] * pos[1]


assert part1(t_course) == 150
print(part1(course))


# PART 2
def part2(course):
    aim = 0
    pos = [0, 0]  # horizontal, depth
    for cmd in course:
        d = cmd[0]
        u = int(cmd[1])
        if d == "forward":
            pos[0] += u
            pos[1] += aim * u
        elif d == "down":
            aim += u
        else:
            aim -= u
    return pos[0] * pos[1]


assert part2(t_course) == 900
print(part2(course))
