from collections import deque
import networkx as nx

G1 = nx.read_edgelist("test_input1.txt", delimiter="-")
G2 = nx.read_edgelist("test_input2.txt", delimiter="-")
G3 = nx.read_edgelist("test_input3.txt", delimiter="-")
G = nx.read_edgelist("input.txt", delimiter="-")


# PART 1
def count_paths(G, start, visited=[]):
    visited.append(start)
    n_paths = 0
    for u in G[start]:
        if u in visited and u.islower():
            continue
        if u == "end":
            n_paths += 1
            continue
        n_paths += count_paths(G, u, visited)
    visited.pop()
    return n_paths


def part1(G):
    n_paths = count_paths(G, "start")
    return n_paths


assert part1(G1) == 10
assert part1(G2) == 19
assert part1(G3) == 226
print(part1(G))


# PART 2
def count_paths2(G, start, visited=[], small=False):
    visited.append(start)
    if start.islower() and visited.count(start) == 2:
        small = True
    n_paths = 0
    for u in G[start]:
        if u == "start":
            continue
        if small:
            if u.islower() and u in visited:
                continue
        if u == "end":
            n_paths += 1
            continue
        n_paths += count_paths2(G, u, visited, small)
    visited.pop()
    return n_paths


def part2(G):
    n_paths = count_paths2(G, "start")
    return n_paths


assert part2(G1) == 36
assert part2(G2) == 103
assert part2(G3) == 3509
print(part2(G))
