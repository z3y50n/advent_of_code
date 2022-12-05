def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    crates = data.split("\n\n")[0]
    moves = data.split("\n\n")[1].split('\n')
    levels = crates.split('\n')
    stacks = [[] for _ in range(int(levels[-1].split()[-1]))]

    k = 0
    for i in range(1, len(levels[0]), 4):
        for j in range(len(levels)-2, -1, -1):
            if levels[j][i] != ' ':
                stacks[k].append(levels[j][i])
        k += 1
    
    return stacks, moves

crates, moves = read_data('input.txt')
t_crates, t_moves = read_data('test_input.txt')

def part1(crates, moves):
    for move in moves:
        size = int(move.split()[1])
        source = int(move.split()[3]) - 1
        dest = int(move.split()[5]) - 1
        for i in range(size):
            crate = crates[source].pop()
            crates[dest].append(crate)
    res = []
    for stack in crates:
        if len(stack):
            res.append(stack[-1])
    return ''.join(res)


assert part1(t_crates, t_moves) == 'CMZ'
print(part1(crates, moves))

crates, moves = read_data('input.txt')
t_crates, t_moves = read_data('test_input.txt')

def part2(crates: list, moves):
    for move in moves:
        size = int(move.split()[1])
        source = int(move.split()[3]) - 1
        dest = int(move.split()[5]) - 1
        elems = crates[source][-size:]
        del crates[source][-size:]
        crates[dest].extend(elems)
    res = []
    for stack in crates:
        if len(stack):
            res.append(stack[-1])
    return ''.join(res)

assert part2(t_crates, t_moves) == 'MCD'
print(part2(crates, moves))