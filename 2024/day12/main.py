from collections import defaultdict


def read_data(filename: str):
    with open(filename, "r") as f:
        garden = f.read().split("\n")
    return garden


type Pos = tuple[int, int]


def part1(garden: list[str]) -> int:
    regions = find_regions(garden)
    return sum(len(region) * calc_perimeter(region) for region in regions)


def part2(garden: list[str]) -> int:
    regions = find_regions(garden)
    return sum(len(region) * calc_sides(region) for region in regions)


def find_regions(garden: list[str]) -> list[list[Pos]]:
    H = len(garden)
    W = len(garden[0])
    regions: list[list[Pos]] = []
    visited: set[Pos] = set()
    for i in range(H):
        for j in range(W):
            if (i, j) not in visited:
                regions.append(find_region(garden, (i, j), visited))
    return regions


def find_region(garden: list[str], p: Pos, visited: set[Pos]) -> list[Pos]:
    H = len(garden)
    W = len(garden[0])
    letter = garden[p[0]][p[1]]
    stack: list[Pos] = [p]
    region: list[Pos] = []
    while stack:
        pos = stack.pop()
        if pos not in visited:
            region.append(pos)
            visited.add(pos)
            for nbr in nbrs(pos):
                if is_valid(nbr, H, W) and garden[nbr[0]][nbr[1]] == letter:
                    stack.append(nbr)
    return region


def calc_perimeter(region: list[Pos]) -> int:
    perimeter = 0
    for pos in region:
        plus = 4
        for nbr in nbrs(pos):
            if nbr in region:
                plus -= 1
        perimeter += plus
    return perimeter


def nbrs(p):
    x, y = p
    return [
        (x - 1, y),
        (x, y + 1),
        (x + 1, y),
        (x, y - 1),
    ]


def is_valid(pos: Pos, H: int, W: int) -> bool:
    x, y = pos
    return 0 <= x < H and 0 <= y < W


def calc_sides(region: list[Pos]) -> int:
    perimeter_points: defaultdict[Pos, list[int]] = defaultdict(list)
    for p in region:
        for direction, nbr in enumerate(nbrs(p)):
            if nbr not in region:
                perimeter_points[nbr].append(direction)

    n_sides = 0
    for p in list(perimeter_points.keys()):
        dirs = perimeter_points[p]
        while len(dirs):
            n_sides += 1
            dir = dirs.pop(0)
            # Clockwise
            current = nbrs(p)[(dir+1) % 4]
            while dir in perimeter_points[current]:
                perimeter_points[current].remove(dir)
                current = nbrs(current)[(dir+1) % 4]
            # Counter-clockwise
            current = nbrs(p)[(dir+3) % 4]
            while dir in perimeter_points[current]:
                perimeter_points[current].remove(dir)
                current = nbrs(current)[(dir-1) % 4]
    return n_sides



if __name__ == "__main__":
    test_garden = read_data("test_input.txt")
    garden = read_data("input.txt")

    assert part1(test_garden) == 1930
    print(part1(garden))

    assert part2(test_garden) == 1206
    print(part2(garden))
