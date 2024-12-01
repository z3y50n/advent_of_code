from collections import Counter

def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read().strip().split('\n')

    return [int(row.split()[0]) for row in data], [int(row.split()[1]) for row in data]


def part1(locs1: list[int], locs2:list[int]) -> int:
    return sum((abs(n1-n2) for n1, n2 in zip(sorted(locs1), sorted(locs2))))


def part2(locs1: list[int], locs2:list[int]) -> int:
    counts = Counter(locs2)
    return sum((n * counts[n] for n in locs1))


if __name__ == "__main__":
    test_locs = read_data('test_input')
    locs = read_data('input')
    assert part1(test_locs[0], test_locs[1]) == 11
    print(part1(locs[0], locs[1]))
    assert part2(test_locs[0], test_locs[1]) == 31
    print(part2(locs[0], locs[1]))