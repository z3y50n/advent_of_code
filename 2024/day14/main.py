import re
import math
import itertools
from collections import Counter


def read_data(filename):
    with open(filename, "r") as f:
        data = f.read().strip().split("\n")
    ret = []
    for robot in data:
        a = re.compile(r"p=(\d+),(\d+) v=(-*\d+),(-*\d+)")
        px, py, vx, vy = map(int, a.findall(robot)[0])
        ret.append((px, py, vx, vy))
    return ret


def part1(robots: list[tuple[int, int, int, int]], w: int, h: int) -> int:
    quads = Counter()
    hw = w // 2
    hh = h // 2
    for px, py, vx, vy in robots:
        x = (px + vx * 100) % w
        y = (py + vy * 100) % h
        if x == hw or y == hh:
            continue
        quads[(x > hw, y > hh)] += 1
    return math.prod(quads.values())


def print_map(pts: list[tuple[int, int]], w: int, h: int):
    for j in range(h):
        for i in range(w):
            if (i, j) in pts:
                print('*', end='')
            else:
                print('.', end='')
        print('\n')


def part2(robots: list[tuple[int, ...]], w: int, h: int) -> int:
    for n in itertools.count():
        pts = [((px + vx * n) % w, (py + vy * n) % h) for px, py, vx, vy in robots]
        # By testing, if no points overlap we get a tree ¯\_(ツ)_/¯
        if len(set(pts)) == len(pts):
            print_map(pts, w, h)
            return n


if __name__ == "__main__":
    test_robots = read_data("test_input.txt")
    robots = read_data("input.txt")

    assert part1(test_robots, 11, 7) == 12
    print(part1(robots, 101, 103))

    part2(robots, 101, 103)