from collections import defaultdict

def read_data(filename):
    with open(filename, "r") as f:
        data = f.read().strip().split("\n")

    return data

ttiles = read_data("test.txt")
tiles = read_data("day24.txt")

directions = {
    "e": (1, 0),
    "se": (0.5, -1),
    "sw": (-0.5, -1),
    "w": (-1, 0),
    "nw": (-0.5, 1),
    "ne": (0.5, 1)
}
    
# PART 1
def part1(tiles):
    positions = defaultdict(lambda: "white")
    for tile in tiles:
        i = 0
        x = 0
        y = 0
        while i < len(tile):
            c = tile[i]
            if c == "s" or c == "n":
                c = tile[i:i+2]
                i += 2
            else:
                i += 1
            mv = directions[c]
            x += mv[0]
            y += mv[1]
        if positions[(x, y)] == "white":
            positions[(x, y)] = "black"
        else:
            positions[(x, y)] = "white"
    return positions

tpositions = part1(ttiles)
print(tpositions)
tcnt = sum(color == "black" for color in tpositions.values())
assert tcnt == 10

positions = part1(tiles)
cnt = sum(color == "black" for color in positions.values())
print(cnt)

# PART 2
def get_neighbours(positions, pos):
    x, y = pos
    for d in directions.values():
        yield positions[(x+d[0], y+d[1])]

def find_limits(positions):
    max_x = 0
    max_y = 0
    min_x = 0
    min_y = 0
    for x, y in positions:
        if x > max_x:
            max_x = x
        if x < min_x:
            min_x = x
        if y > max_y:
            max_y = y
        if y < min_y:
            min_y = y
    return max_x+1, max_y+1, min_x-1, min_y-1

def traverse(positions):
    max_x, max_y, min_x, min_y = find_limits(positions)
    def next_tile(x, y):
        x += 0.5
        if x == max_x + 0.5:
            x = min_x
            y += 1
        return x, y
    x, y = next_tile(min_x-0.5, min_y) 
    while y <= max_y:
        yield (x, y)
        x, y = next_tile(x, y)

def part2(positions):
    for _ in range(100):
        new = positions.copy()
        for pos in traverse(positions):
            color = positions[pos]
            cnt = 0
            for n in get_neighbours(positions, pos):
                if n == "black": cnt += 1
            if color == "black" and (cnt == 0 or cnt > 2):
                new[pos] = "white"
            elif color == "white" and cnt == 2:
                new[pos] = "black"
        positions = new.copy()
    return new

tpositions = part2(tpositions)
tcnt = sum(color == "black" for color in tpositions.values())
assert tcnt == 2208

positions = part2(positions)
cnt = sum(color == "black" for color in positions.values())
print(cnt)

