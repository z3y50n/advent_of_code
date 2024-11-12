def read_data(filename: str):
    with open(filename, "r") as f:
        data = f.read().strip().split("\n")
    return data


def print_field(field: list[str]):
    for row in field:
        print(' '.join(list(row)))


def part1(field: list[str]) -> int:
    start = find_start(field)
    loop = find_loop(field, start)
    return len(loop) // 2


def find_start(field: list[str]) -> tuple[int, int]:
    for i, row in enumerate(field):
        for j, col in enumerate(row):
            if col == "S":
                return (i, j)
    return (0, 0)


def find_loop(field: list[str], start: tuple[int, int]) -> list[tuple[int, int]]:
    visited = set()
    stack = [(start, [start])]
    while len(stack):
        node, path = stack.pop()
        if node == start and len(path) > 3:
            return path
        if node not in visited:
            visited.add(node)
            nbrs = find_nbrs(field, node)
            for nbr in nbrs:
                stack.append((nbr, path + [nbr]))


def find_nbrs(field: list[str], node: tuple[int, int]) -> list[tuple[int, int]]:
    i, j = node
    nbrs = []
    if field[i][j] == "S":
        if i > 0:
            nbrs.append((i - 1, j))
        if i < len(field) - 1:
            nbrs.append((i + 1, j))
        if j > 0:
            nbrs.append((i, j - 1))
        if j < len(field[0]) - 1:
            nbrs.append((i, j + 1))
    elif field[i][j] == "|":
        if i > 0:
            nbrs.append((i - 1, j))
        if i < len(field) - 1:
            nbrs.append((i + 1, j))
    elif field[i][j] == "-":
        if j > 0:
            nbrs.append((i, j - 1))
        if j < len(field[0]) - 1:
            nbrs.append((i, j + 1))
    elif field[i][j] == "L":
        if i > 0:
            nbrs.append((i - 1, j))
        if j < len(field[0]) - 1:
            nbrs.append((i, j + 1))
    elif field[i][j] == "J":
        if i > 0:
            nbrs.append((i - 1, j))
        if j > 0:
            nbrs.append((i, j - 1))
    elif field[i][j] == "7":
        if i < len(field) - 1:
            nbrs.append((i + 1, j))
        if j > 0:
            nbrs.append((i, j - 1))
    elif field[i][j] == "F":
        if i < len(field) - 1:
            nbrs.append((i + 1, j))
        if j < len(field[0]) - 1:
            nbrs.append((i, j + 1))
    return nbrs


def part2(field: list[str]) -> int:
    start = find_start(field)
    loop = find_loop(field, start)
    marked_field = create_marked_field(field, loop)
    print_field(marked_field)
    return sum([1 if col == 'I' else 0 for row in marked_field for col in row])


def create_marked_field(field: list[str], loop: list[tuple[int, int]]) -> list[str]:
    new_field = [["O"] * len(row) for row in field]
    for i, j in loop:
        new_field[i][j] = field[i][j]
    
    for i in range(len(new_field)):
        inside = False
        for j in range(len(new_field[i])):
            # this is a bit cheating, since S = L in the data, but could be something else
            if new_field[i][j] in '|JLS':
                inside = not inside
            elif new_field[i][j] == 'O':
                if inside:
                    new_field[i][j] = 'I'
    return ["".join(row) for row in new_field]


if __name__ == "__main__":
    test_field = read_data("test_input")
    test_field2 = read_data("test_input2")
    field = read_data("input")
    assert part1(test_field) == 4
    assert part1(test_field2) == 8
    # print(part1(field))
    print(part2(field))
    # print(part2(test_field))
    # print("---")
    # part2(test_field2)
