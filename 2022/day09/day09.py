def read_data(filename):
    with open(filename, "r") as f:
        data = f.read().strip().split("\n")
    return list(map(lambda x: (x.split()[0], int(x.split()[1])), data))


t_moves = read_data("test_input.txt")
t_moves2 = read_data("test_input2.txt")
moves = read_data("input.txt")


def move_head(direction, pos):
    if direction == "R":
        return (pos[0] + 1, pos[1])
    if direction == "L":
        return (pos[0] - 1, pos[1])
    if direction == "U":
        return (pos[0], pos[1] + 1)
    return (pos[0], pos[1] - 1)


def are_touching(pos1, pos2):
    if abs(pos1[0] - pos2[0]) <= 1 and abs(pos1[1] - pos2[1]) <= 1:
        return True
    return False


def sign(x):
    if x == 0:
        return 0
    return int(x / abs(x))


def move_tail(h_pos, t_pos):
    if are_touching(h_pos, t_pos):
        return t_pos
    dx = h_pos[0] - t_pos[0]
    dy = h_pos[1] - t_pos[1]
    return (t_pos[0] + 1 * sign(dx), t_pos[1] + 1 * sign(dy))


def part1(moves):
    h_pos = (0, 0)
    t_pos = (0, 0)
    visited = {(0, 0)}
    for move in moves:
        for _ in range(move[1]):
            h_pos = move_head(move[0], h_pos)
            t_pos = move_tail(h_pos, t_pos)
            visited.add(t_pos)
    return len(visited)


assert part1(t_moves) == 13
print(part1(moves))


def part2(moves):
    rope = [(0, 0) for _ in range(10)]
    visited = {(0, 0)}
    for move in enumerate(moves):
        for _ in range(move[1]):
            for i in range(10):
                if i == 0:
                    rope[i] = move_head(move[0], rope[0])
                else:
                    rope[i] = move_tail(rope[i - 1], rope[i])
            visited.add(rope[-1])
    return len(visited)


assert part2(t_moves2) == 36
print(part2(moves))
