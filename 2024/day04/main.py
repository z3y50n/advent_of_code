def read_data(filename):
    with open(filename, "r") as f:
        data = f.read().strip().split("\n")
    return [list(row) for row in data]


def part1(layout: list[list[str]]):
    H = len(layout)
    W = len(layout[0])
    r = 0
    for i in range(H):
        for j in range(W):
            if (
                j <= W - 4
                and layout[i][j] == "X"
                and layout[i][j + 1] == "M"
                and layout[i][j + 2] == "A"
                and layout[i][j + 3] == "S"
            ):
                r += 1
            if (
                i <= H - 4
                and layout[i][j] == "X"
                and layout[i + 1][j] == "M"
                and layout[i + 2][j] == "A"
                and layout[i + 3][j] == "S"
            ):
                r += 1
            if (
                j >= 3
                and layout[i][j] == "X"
                and layout[i][j - 1] == "M"
                and layout[i][j - 2] == "A"
                and layout[i][j - 3] == "S"
            ):
                r += 1
            if (
                i >= 3
                and layout[i][j] == "X"
                and layout[i - 1][j] == "M"
                and layout[i - 2][j] == "A"
                and layout[i - 3][j] == "S"
            ):
                r += 1
            if (
                i <= H - 4
                and j <= W - 4
                and layout[i][j] == "X"
                and layout[i + 1][j + 1] == "M"
                and layout[i + 2][j + 2] == "A"
                and layout[i + 3][j + 3] == "S"
            ):
                r += 1
            if (
                i <= H - 4
                and j >= 3
                and layout[i][j] == "X"
                and layout[i + 1][j - 1] == "M"
                and layout[i + 2][j - 2] == "A"
                and layout[i + 3][j - 3] == "S"
            ):
                r += 1
            if (
                i >= 3
                and j <= W - 4
                and layout[i][j] == "X"
                and layout[i - 1][j + 1] == "M"
                and layout[i - 2][j + 2] == "A"
                and layout[i - 3][j + 3] == "S"
            ):
                r += 1
            if (
                i >= 3
                and j >= 3
                and layout[i][j] == "X"
                and layout[i - 1][j - 1] == "M"
                and layout[i - 2][j - 2] == "A"
                and layout[i - 3][j - 3] == "S"
            ):
                r += 1
    return r


def part2(layout: list[list[str]]) -> int:
    H = len(layout)
    W = len(layout[0])
    r = 0
    for i in range(1, H - 1):
        for j in range(1, W - 1):
            if layout[i][j] == "A":
                if (
                    (layout[i - 1][j - 1] == "M" and layout[i + 1][j + 1] == "S")
                    or (layout[i - 1][j - 1] == "S" and layout[i + 1][j + 1] == "M")
                ) and (
                    (layout[i - 1][j + 1] == "M" and layout[i + 1][j - 1] == "S")
                    or (layout[i - 1][j + 1] == "S" and layout[i + 1][j - 1] == "M")
                ):
                    r += 1
    return r


if __name__ == "__main__":
    test_layout = read_data("test_input")
    layout = read_data("input")
    assert part1(test_layout) == 18
    print(part1(layout))
    assert part2(test_layout) == 9
    print(part2(layout))
