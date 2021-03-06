import numpy as np
import networkx as nx


t_cavern = np.genfromtxt("test_input.txt", dtype=int, delimiter=1)
cavern = np.genfromtxt("input.txt", dtype=int, delimiter=1)


def G_from_array(cavern):
    G = nx.DiGraph()
    for i in range(cavern.shape[0]):
        for j in range(cavern.shape[1]):
            if j != 0:
                G.add_edge((i, j), (i, j - 1), weight=cavern[i, j - 1])
            if i != 0:
                G.add_edge((i, j), (i - 1, j), weight=cavern[i - 1, j])
            if j != cavern.shape[1] - 1:
                G.add_edge((i, j), (i, j + 1), weight=cavern[i, j + 1])
            if i != cavern.shape[0] - 1:
                G.add_edge((i, j), (i + 1, j), weight=cavern[i + 1, j])
    return G


def solve(cavern):
    G = G_from_array(cavern)
    target = (cavern.shape[0] - 1, cavern.shape[1] - 1)
    return nx.shortest_path_length(G, source=(0, 0), target=target, weight="weight")


# PART 1
def part1(cavern):
    return solve(cavern)


assert part1(t_cavern) == 40
print(part1(cavern))


# PART 2
def full_map(cavern):
    N, M = cavern.shape
    full_cavern = np.tile(cavern, (5, 5))
    for i in range(5):
        for j in range(5):
            if i + j == 0:
                continue
            full_cavern[i * N : i * N + N, j * M : j * M + M] = (cavern + i + j) % 9

    full_cavern[full_cavern == 0] = 9
    return full_cavern


def part2(cavern):
    full_cavern = full_map(cavern)
    return solve(full_cavern)


assert part2(t_cavern) == 315
print(part2(cavern))
