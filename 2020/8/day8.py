def read_data(filename):
    with open(filename, "r") as f:
        data = f.read().split("\n")[:-1]

    commands = [[command.split(" ")[0], int(command.split(" ")[1])] for command in data]
    return commands

commands = read_data("day8.txt")

# PART 1
def part_1(commands):
    visited = []
    pos = 0
    acc = 0
    while pos not in visited and pos < len(commands):
        visited.append(pos)
        if commands[pos][0] == "nop":
            pos += 1
        elif commands[pos][0] == "acc":
            acc += commands[pos][1]
            pos += 1
        elif commands[pos][0] == "jmp":
            pos += commands[pos][1]
    return acc, pos

print(part_1(commands))

# PART 2
def part_2(commands):
    for i, command in enumerate(commands):
        if command[0] == "acc":
            continue
        else:
            if command[0] == "nop":
                commands[i][0] = "jmp"
                saved = "nop"
            else:
                commands[i][0] = "nop"
                saved = "jmp"
        #run
        acc, pos = part_1(commands)
        if pos >= len(commands): return acc

        #restore command
        commands[i][0] = saved


print(part_2(commands))
