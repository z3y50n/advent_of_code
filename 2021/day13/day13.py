import numpy as np

np.set_printoptions(edgeitems=30, linewidth=100000)


def read_data(filename):
    with open(filename, "r") as f:
        coords, folds = f.read().strip().split("\n\n")
    coords = [tuple(map(int, coord.split(","))) for coord in coords.split("\n")]
    folds = [(fold[11], int(fold[13:])) for fold in folds.split("\n")]
    return coords, folds


# Initialize data
t_coords, t_folds = read_data("test_input.txt")
coords, folds = read_data("input.txt")


def find_dims(coords):
    N = max(coords, key=lambda x: x[1])[1] + 1
    M = max(coords, key=lambda x: x[0])[0] + 1

    return N, M


def fill_board(coords, N, M):
    board = np.full((N, M), fill_value=".")

    for coord in coords:
        board[coord[1], coord[0]] = "#"
    return board


N_t, M_t = find_dims(t_coords)
N, M = find_dims(coords)
t_board = fill_board(t_coords, N_t, M_t)
board = fill_board(coords, N, M)


def merge_v(board1, board2):
    end = board2.shape[1]
    bigger = False
    if board2.shape[1] > board1.shape[1]:
        end = board1.shape[1]
        bigger = True
    for y in range(board2.shape[0]):
        for x in range(board2.shape[1]):
            if board2[y, x] == "#":
                board1[y, board2.shape[1] - 1 - x] = "#"
    if bigger:
        board1 = np.hstack((board2[:, end:], board1))
    return board1


def merge_h(board1, board2):
    end = board2.shape[0]
    bigger = False
    if board2.shape[0] > board1.shape[0]:
        end = board1.shape[0]
        bigger = True
    for y in range(end):
        for x in range(board2.shape[1]):
            if board2[y, x] == "#":
                board1[board2.shape[0] - 1 - y, x] = "#"
    if bigger:
        board1 = np.vstack((board2[end:, :], board1))
    return board1


def solve(board, folds, part1=True):
    for fold in folds:
        if fold[0] == "x":
            board1 = board[:, : fold[1]]
            board2 = board[:, fold[1] + 1 :]
            merged = merge_v(board1, board2)
        if fold[0] == "y":
            board1 = board[: fold[1], :]
            board2 = board[fold[1] + 1 :, :]
            merged = merge_h(board1, board2)
        board = merged
        if part1:
            break
    if part1:
        return np.sum(board == "#")
    else:
        print(board)


assert solve(t_board, t_folds) == 17
print(solve(board.copy(), folds))

solve(board, folds, part1=False)
