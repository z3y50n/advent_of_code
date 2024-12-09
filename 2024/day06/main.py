from enum import IntEnum


def read_data(filename):
    with open(filename, "r") as f:
        data = f.read().strip().split("\n")
    return data


class Direction:
    Up = 0
    Right = 1
    Down = 2
    Left = 3


def part1(area: list[str]) -> int:
    H = len(area)
    W = len(area[0])
    guard = find_guard(area)
    direction = Direction.Up
    visited: set[tuple[int, int]] = set()
    while 0 <= guard[0] < H and 0 <= guard[1] < W:
        visited.add(guard)
        if direction == Direction.Up:
            i, j = guard
            if i > 0 and area[i - 1][j] == "#":
                direction = (direction + 1) % 4
            else:
                guard = (i - 1, j)
        elif direction == Direction.Right:
            i, j = guard
            if j < W - 1 and area[i][j + 1] == "#":
                direction = (direction + 1) % 4
            else:
                guard = (i, j + 1)
        elif direction == Direction.Down:
            i, j = guard
            if i < H - 1 and area[i + 1][j] == "#":
                direction = (direction + 1) % 4
            else:
                guard = (i + 1, j)
        elif direction == Direction.Left:
            i, j = guard
            if j > 0 and area[i][j - 1] == "#":
                direction = (direction + 1) % 4
            else:
                guard = (i, j - 1)
    return len(visited), visited


def part2(area: list[str], main_path: set[tuple[int, int]]) -> int:
    H = len(area)
    W = len(area[0])
    init_guard = find_guard(area)
    main_path.remove(init_guard)
    ret = 0
    for obst in main_path:
        guard = init_guard
        direction = Direction.Up
        visited: set[tuple[int, int, Direction]] = set()
        while 0 <= guard[0] < H and 0 <= guard[1] < W:
            if ((*guard, direction) in visited):
                ret += 1
                break
            visited.add((*guard, direction))
            if direction == Direction.Up:
                i, j = guard
                if (i - 1, j) == obst or i > 0 and area[i - 1][j] == "#":
                    direction = (direction + 1) % 4
                else:
                    guard = (i - 1, j)
            elif direction == Direction.Right:
                i, j = guard
                if (i, j + 1) == obst or j < W - 1 and area[i][j + 1] == "#":
                    direction = (direction + 1) % 4
                else:
                    guard = (i, j + 1)
            elif direction == Direction.Down:
                i, j = guard
                if (i + 1, j) == obst or i < H - 1 and area[i + 1][j] == "#":
                    direction = (direction + 1) % 4
                else:
                    guard = (i + 1, j)
            elif direction == Direction.Left:
                i, j = guard
                if (i, j - 1) == obst or j > 0 and area[i][j - 1] == "#":
                    direction = (direction + 1) % 4
                else:
                    guard = (i, j - 1)

    return ret


def find_guard(area: list[str]) -> tuple[int, int]:
    H = len(area)
    W = len(area[0])
    for i in range(H):
        for j in range(W):
            if area[i][j] == "^":
                return (i, j)


if __name__ == "__main__":
    test_area = read_data("test_input")
    area = read_data("input")

    t_pos, t_visited = part1(test_area)
    pos, visited = part1(area)
    assert t_pos == 41
    print(pos)

    assert part2(test_area, t_visited) == 6
    # Takes a few seconds to run
    print(part2(area, visited))
