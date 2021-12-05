def read_data(filename):
    with open(filename, "r") as f:
        data = f.read().strip().split("\n")
    lines = [[list(map(int, i.split(","))) for i in x.split(" -> ")] for x in data]
    return lines


t_lines = read_data("test_input.txt")
lines = read_data("input.txt")


def is_horizontal(line):
    if line[0][0] == line[1][0]:
        return True
    return False


def is_vertical(line):
    if line[0][1] == line[1][1]:
        return True
    return False


def print_board(board):
    for row in board:
        print(row)


# PART 1
def part1(lines):
    board = [[0 for j in range(1000)] for i in range(1000)]  # 1000 is cheating:P
    for line in lines:
        if is_horizontal(line):
            f_y = min(line[0][1], line[1][1])
            t_y = max(line[0][1], line[1][1])
            for i in range(f_y, t_y + 1):
                board[i][line[0][0]] += 1
        elif is_vertical(line):
            f_x = min(line[0][0], line[1][0])
            t_x = max(line[0][0], line[1][0])
            for i in range(f_x, t_x + 1):
                board[line[0][1]][i] += 1
    return sum(i > 1 for row in board for i in row)


assert part1(t_lines) == 5
print(part1(lines))

# PART 2
def part2(lines):
    board = [[0 for j in range(1000)] for i in range(1000)]  # 1000 is cheating:P
    for line in lines:
        f_x = line[0][0]
        f_y = line[0][1]
        t_x = line[1][0]
        t_y = line[1][1]
        x_step = 1 if f_x < t_x else -1
        y_step = 1 if f_y < t_y else -1
        if is_vertical(line):
            y_step = 0
        if is_horizontal(line):
            x_step = 0

        while f_x != t_x or f_y != t_y:
            board[f_y][f_x] += 1
            f_x += x_step
            f_y += y_step
        board[f_y][f_x] += 1

    return sum(i > 1 for row in board for i in row)


assert part2(t_lines) == 12
print(part2(lines))
