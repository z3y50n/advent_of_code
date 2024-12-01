def read_data(filename):
    with open(filename, "r") as f:
        data = f.read().strip().split("\n")
    return [list(row) for row in data]


def print_platform(platform):
    for row in platform:
        print("".join(row))


def part1(platform: list[list[str]]) -> int:
    h = len(platform)
    w = len(platform[0])
    res = 0
    for j in range(w):
        column = [row[j] for row in platform]
        last_barrier = -1
        for i, tile in enumerate(column):
            if tile == "#":
                last_barrier = i
            elif tile == "O":
                last_barrier += 1
                res += h - last_barrier
    return res


def hash_platform(platform: list[list[str]]):
    return "".join("".join(row) for row in platform)


def part2(platform: list[list[str]]):
    N = 1000000000
    new_platform = platform.copy()
    cache = set()
    cache.add(hash_platform(platform))
    first_same = ""
    first_cycle = 0
    for cycle in range(N):
        new_platform = make_cycle(new_platform)

        if hash_platform(new_platform) == first_same:
            loop_length = cycle - first_cycle
            new_n = (N - first_cycle - 1) % loop_length
            for _ in range(new_n):
                new_platform = make_cycle(new_platform)
            return calc_weight(new_platform)

        if first_same == "" and hash_platform(new_platform) in cache:
            first_cycle = cycle
            first_same = hash_platform(new_platform)
            break
        cache.add(hash_platform(new_platform[::]))


def calc_weight(platform: list[list[str]]):
    H = len(platform)
    W = len(platform[0])
    return sum(H - i for i in range(H) for j in range(W) if platform[i][j] == "O")


def make_cycle(platform: list[list[str]]):
    H = len(platform)
    W = len(platform[0])
    new_platform = platform.copy()
    for j in range(W):
        column = [row[j] for row in new_platform]
        new_col = move_tiles(column)
        for i in range(H):
            new_platform[i][j] = new_col[i]
    for i in range(H):
        new_row = move_tiles(new_platform[i])
        for j in range(W):
            new_platform[i][j] = new_row[j]
    for j in range(W):
        column = [row[j] for row in new_platform][::-1]
        new_col = move_tiles(column)[::-1]
        for i in range(H):
            new_platform[i][j] = new_col[i]
    for i in range(H):
        new_row = move_tiles(new_platform[i][::-1])[::-1]
        for j in range(W):
            new_platform[i][j] = new_row[j]
    return new_platform


def move_tiles(tiles: list[str]):
    new = tiles.copy()
    last_barrier = -1
    for i, tile in enumerate(tiles):
        if tile == "#":
            last_barrier = i
        elif tile == "O":
            new[i] = "."
            new[last_barrier + 1] = "O"
            last_barrier += 1
    return new


if __name__ == "__main__":
    test_platform = read_data("test_input")
    platform = read_data("input")
    assert part1(test_platform) == 136
    print(part1(platform))

    assert part2(test_platform) == 64
    print(part2(platform))
