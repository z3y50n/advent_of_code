from enum import IntEnum


def read_data(filename):
    with open(filename, "r") as f:
        data = f.read().strip().split("\n")
    return [list(row) for row in data]


class Direction(IntEnum):
    Right = 0
    Bot = 1
    Left = 2
    Top = 3


def part1(layout: list[list[str]]) -> int:
    stack: list[tuple[int, int, Direction]] = [(0, 0, Direction.Right)]
    visited: set[tuple[int, int, Direction]] = set()
    energized: set[tuple[int, int]] = set()
    while len(stack):
        i, j, dir = stack.pop()
        visited.add((i, j, dir))
        energized.add((i, j))
        for nbr in get_nbrs(layout, i, j, dir):
            if nbr not in visited:
                stack.append(nbr)
    return len(energized)


def get_nbrs(
    layout: list[list[str]], i: int, j: int, dir: Direction
) -> list[tuple[int, int, Direction]]:
    H = len(layout)
    W = len(layout[0])
    if layout[i][j] == ".":
        return keep_direction(H, W, i, j, dir)
    if layout[i][j] == '-':
        if dir == Direction.Left or dir == Direction.Right:
            return keep_direction(H, W, i, j, dir)
        else:
            ret = []
            if j > 0:
                ret.append((i, j-1, Direction.Left))
            if j < W - 1:
                ret.append((i, j+1, Direction.Right))
            return ret
    if layout[i][j] == '|':
        if dir == Direction.Top or dir == Direction.Bot:
            return keep_direction(H, W, i, j, dir)
        else:
            ret = []
            if i > 0:
                ret.append((i-1, j, Direction.Top))
            if i < H - 1:
                ret.append((i+1, j, Direction.Bot))
            return ret
    if layout[i][j] == '/':
        if dir == Direction.Left and i < H - 1:
            return [(i+1, j, Direction.Bot)]
        elif dir == Direction.Right and i > 0:
            return [(i-1, j, Direction.Top)]
        elif dir == Direction.Top and j < W - 1:
            return [(i, j+1, Direction.Right)]
        elif dir == Direction.Bot and j > 0:
            return [(i, j-1, Direction.Left)]
        return []
    if layout[i][j] == '\\':
        if dir == Direction.Left and i > 0:
            return [(i-1, j, Direction.Top)]
        elif dir == Direction.Right and i < H - 1:
            return [(i+1, j, Direction.Bot)]
        elif dir == Direction.Top and j > 0:
            return [(i, j-1, Direction.Left)]
        elif dir == Direction.Bot and j < W - 1:
            return [(i, j+1, Direction.Right)]
        return []


def keep_direction(H, W, i, j, dir) -> list[tuple[int, int, Direction]]:
    if dir == Direction.Right and j < W - 1:
        return [(i, j + 1, Direction.Right)]
    if dir == Direction.Left and j > 0:
        return [(i, j - 1, Direction.Left)]
    if dir == Direction.Top and i > 0:
        return [(i - 1, j, Direction.Top)]
    if dir == Direction.Bot and i < H - 1:
        return [(i + 1, j, Direction.Bot)]
    return []


if __name__ == "__main__":
    test_layout = read_data("test_input")
    layout = read_data("input")
    assert part1(test_layout) == 46
    print(part1(layout))
