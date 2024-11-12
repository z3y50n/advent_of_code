def read_data(filename: str):
    with open(filename, "r") as f:
        data = f.read().strip().split("\n")
    return list(map(list, data))


def print_galaxy(galaxy):
    for row in galaxy:
        print(" ".join(list(row)))


def solution(galaxy: list[list[str]], n_expand: int) -> int:
    stars = find_stars(galaxy)
    expand_rows = find_expand_rows(galaxy)
    expand_cols = find_expand_cols(galaxy)
    res = 0
    for i, star in enumerate(stars):
        for pair in stars[i + 1 :]:
            diff_x = abs(star[0] - pair[0])
            diff_y = abs(star[1] - pair[1])
            add_row = 0
            for exp_row in expand_rows:
                if (
                    abs(exp_row - star[0]) <= diff_x
                    and abs(exp_row - pair[0]) <= diff_x
                ):
                    add_row += n_expand - 1
            add_col = 0
            for exp_col in expand_cols:
                if (
                    abs(exp_col - star[1]) <= diff_y
                    and abs(exp_col - pair[1]) <= diff_y
                ):
                    add_col += n_expand - 1
            res += diff_x + diff_y + add_col + add_row
    return res


def find_expand_cols(galaxy: list[list[str]]) -> list[int]:
    return [
        col
        for col in range(len(galaxy[0]))
        if all([galaxy[row][col] == "." for row in range(len(galaxy))])
    ]


def find_expand_rows(galaxy: list[list[str]]) -> list[int]:
    return [row for row in range(len(galaxy)) if all([x == "." for x in galaxy[row]])]


def find_stars(galaxy: list[list[str]]) -> list[tuple[int, int]]:
    return [
        (i, j)
        for i in range(len(galaxy))
        for j in range(len(galaxy[i]))
        if galaxy[i][j] == "#"
    ]


if __name__ == "__main__":
    test_galaxy = read_data("test_input")
    galaxy = read_data("input")

    assert solution(test_galaxy, 2) == 374
    print(solution(galaxy, 2))

    print(solution(galaxy, 1000000))
