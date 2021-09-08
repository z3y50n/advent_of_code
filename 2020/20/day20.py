from math import sqrt
import numpy as np

def read_data(filename):
    with open(filename, "r") as f:
        data = f.read()[:-1].split("\n\n")

    tiles = {}
    for tile in data:
        rows = tile.split("\n")
        t_id = int(rows[0][5:-1])
        rows = [list(row) for row in rows[1:]]
        tiles[t_id] = np.array(rows)
    return tiles


tiles = read_data("testa.txt")
#tiles = read_data("day20.txt")
N_ROWS = N_COLS = int(sqrt(len(tiles)))
board = np.zeros(len(tiles), dtype=int).reshape(N_ROWS, N_COLS)
images = [[0] * N_COLS for _ in range(N_ROWS)]

# PART 1 (Find Only Corner Pieces)
def get_borders(img):
    """Get all 8 possible borders of an image"""
    return [
        img[0, :],
        img[:, 0],
        img[-1, :],
        img[:, -1],
        np.fliplr(img)[0, :],
        np.fliplr(img)[-1, :],
        np.flipud(img)[:, 0],
        np.flipud(img)[:, -1],
    ]

def find_neighbours(tiles):
    """UGLY"""
    nbrs = {t_id: 0 for t_id in tiles}
    for t_id, img in tiles.items():
        borders1 = get_borders(img)
        for t_id2, img2 in tiles.items():
            if t_id == t_id2:
                continue
            borders2 = get_borders(img2)
            for b1 in borders1:
                for b2 in borders2:
                    if np.array_equal(b1, b2):
                        nbrs[t_id] += 1
    return nbrs

def part1(nbrs):
    prod = 1
    for nbr, cnt in nbrs.items():
        if cnt == 4:
            prod *= nbr
    return prod

nbrs = find_neighbours(tiles)
corners = [nbr for nbr, cnt in nbrs.items() if cnt == 4]
corners = {t_id: tiles[t_id] for t_id in corners}
print(part1(nbrs))

# PART 2 (Backtracking assemble the image)
def next(img):
    combinations = [
        img,
        np.rot90(img),
        np.rot90(img, 2),
        np.rot90(img, 3),
        np.flipud(img),
        np.rot90(np.flipud(img)),
        np.rot90(np.flipud(img), 2),
        np.rot90(np.flipud(img), 3)
    ]
    return combinations

def reject(img, i, j):
    row = img[0, :]
    col = img[:, 0]
    if i == 0 and j == 0:
        return False
    elif i == 0 and j > 0:
        check = images[i][j-1]
        check_col = check[:, -1]
        return not np.array_equal(col, check_col)
    elif i > 0 and j == 0:
        check = images[i-1][j]
        check_row = check[-1, :]
        return not np.array_equal(row, check_row)
    else:
        check1 = images[i][j-1]
        check2 = images[i-1][j]
        check_col = check1[:, -1]
        check_row = check2[-1, :]
        return not (np.array_equal(row, check_row) and np.array_equal(col, check_col))

def is_corner(i, j):
    return (
        (i == j == 0)
        or (i == 0 and j == N_COLS - 1)
        or (i == N_ROWS - 1 and j == 0)
        or (i == N_ROWS - 1 and j == N_COLS - 1)
    )

def accept():
    return board.all()

def next_pos(i, j):
    x = i
    y = j + 1
    if y == N_COLS:
        x += 1
        y = 0
    return x, y

def solve(i=0, j=-1):
    i, j = next_pos(i, j)
    if accept():
        return True
    source = tiles.copy()
    if is_corner(i, j):
        source = corners.copy()
    for id, tile in source.items():
        comb = next(tile)
        if id in board:
            continue
        for img in comb:
            if not reject(img, i, j):
                board[i][j] = id
                images[i][j] = img
                if solve(i, j):
                    return True
                board[i][j] = 0
                images[i][j] = 0
    return False

def strip_border(img):
    return img[1:-1, 1:-1]

def assemble_img(images):
    image = np.zeros(N_ROWS*8*N_COLS*8, dtype=str).reshape(8*N_ROWS, 8*N_COLS)
    for i, row in enumerate(images):
        for j, img in enumerate(row):
            img = strip_border(img)
            image[i*8:i*8+8, j*8:j*8+8] = img
    return image

pattern = [(18, 0), (0, 1), (5, 1), (6, 1), (11, 1), (12, 1), (17, 1), (18, 1), (19, 1), (1, 2), (4, 2), (7, 2), (10, 2), (13, 2), (16, 2)]
m_width = 20
m_height = 3

def find_monster(image, i, j):
    if j + m_width > image.shape[1]:
        return False
    if i + m_height > image.shape[0]:
        return False
    for pt in pattern:
        if image[i+pt[1], j+pt[0]] != "#":
            return False
    return True

if solve(): print(board)
else: exit(0)

image = assemble_img(images)

def part2(image):
    for img in next(image):
        cnt = 0
        for i in range(img.shape[0] - m_height):
            for j in range(img.shape[1] - m_width):
                if find_monster(img, i, j):
                    cnt += 1
        if cnt:
            return np.count_nonzero(img=="#") - cnt*15

print(part2(image))
