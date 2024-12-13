def read_data(filename):
    with open(filename, "r") as f:
        data = f.read().strip().split("\n")

    return data


def part1(mapp: list[str]) -> int:
    H = len(mapp)
    W = len(mapp[0])
    antennas = find_antennas(mapp, H, W)
    antinodes = set()
    for positions in antennas.values():
        for A in range(len(positions) - 1):
            for B in range(A + 1, len(positions)):
                pos_A = positions[A]
                pos_B = positions[B]
                diff_i = pos_A[0] - pos_B[0]
                diff_j = pos_A[1] - pos_B[1]
                antinode_1 = (pos_A[0] + diff_i, pos_A[1] + diff_j)
                antinode_2 = (pos_B[0] - diff_i, pos_B[1] - diff_j)
                if is_valid_pos(antinode_1, H, W):
                    antinodes.add(antinode_1)
                if is_valid_pos(antinode_2, H, W):
                    antinodes.add(antinode_2)
    return len(antinodes)


def find_antennas(mapp: list[str], H: int, W: int) -> dict[str, list[tuple[int, int]]]:
    antennas: dict[str, list[tuple[int, int]]] = {}
    for i in range(H):
        for j in range(W):
            l = mapp[i][j]
            if l == ".":
                continue
            if l in antennas:
                antennas[l].append((i, j))
            else:
                antennas[l] = [(i, j)]
    return antennas


def part2(mapp: list[str]) -> int:
    H = len(mapp)
    W = len(mapp[0])
    antennas = find_antennas(mapp, H, W)
    antinodes = set()
    for nodes in antennas.values():
        N = len(nodes)
        for i in range(N - 1):
            for j in range(i + 1, N):
                x0, y0 = nodes[i]
                x1, y1 = nodes[j]
                slope = (y1 - y0) / (x1 - x0)
                for x in range(H):
                    y = y0 + slope * (x - x0)
                    if y.is_integer() and is_valid_pos((x, y), H, W):
                        antinodes.add((x, y))
    return len(antinodes)


def is_valid_pos(pos: tuple[int, int], H: int, W: int) -> bool:
    return 0 <= pos[0] < H and 0 <= pos[1] < W


if __name__ == "__main__":
    test_mapp = read_data("test_input.txt")
    mapp = read_data("input.txt")

    assert part1(test_mapp) == 14
    print(part1(mapp))

    assert part2(test_mapp) == 34
    print(part2(mapp))
