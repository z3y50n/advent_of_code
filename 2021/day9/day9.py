def read_data(filename):
    with open(filename, "r") as f:
        data = f.read().strip().split("\n")

    return [list(map(int, list(row))) for row in data]


t_heightmap = read_data("test_input.txt")
heightmap = read_data("input.txt")


def find_nbrs(heightmap, i, j, mode="nbrs"):
    n = len(heightmap)
    m = len(heightmap[0])
    nbrs = []
    nbr_pos = []
    if i > 0:
        nbrs.append(heightmap[i - 1][j])
        nbr_pos.append((i - 1, j))
    if i < n - 1:
        nbrs.append(heightmap[i + 1][j])
        nbr_pos.append((i + 1, j))
    if j > 0:
        nbrs.append(heightmap[i][j - 1])
        nbr_pos.append((i, j - 1))
    if j < m - 1:
        nbrs.append(heightmap[i][j + 1])
        nbr_pos.append((i, j + 1))
    if mode == "nbrs":
        return nbrs
    elif mode == "pos":
        return nbr_pos
    else:
        raise Exception("Mode is either 'nbrs' or 'pos'")


# PART 1
def part1(heightmap):
    n = len(heightmap)
    m = len(heightmap[0])
    lowpoints = []  # will be used for part 2
    s = 0
    for i in range(n):
        for j in range(m):
            num = heightmap[i][j]
            nbrs = find_nbrs(heightmap, i, j)
            if num < min(nbrs):
                lowpoints.append((i, j))
                s += num + 1
    return s, lowpoints


assert part1(t_heightmap)[0] == 15
print(part1(heightmap)[0])

t_lowpoints = part1(t_heightmap)[1]
lowpoints = part1(heightmap)[1]

# PART 2 (Using DFS)
def dfs(heightmap, i, j):
    s = 0
    val = heightmap[i][j]
    heightmap[i][j] = -1
    for x, y in find_nbrs(heightmap, i, j, "pos"):
        if heightmap[x][y] == -1:
            continue
        if heightmap[x][y] > val and heightmap[x][y] != 9:
            s += dfs(heightmap, x, y) + 1
    return s


def part2(heightmap, lowpoints):
    basins = []
    for i, j in lowpoints:
        basins.append(dfs(heightmap, i, j) + 1)
    mult = 1
    for b in sorted(basins)[-3:]:
        mult *= b
    return mult


assert part2(t_heightmap, t_lowpoints) == 1134
print(part2(heightmap, lowpoints))
