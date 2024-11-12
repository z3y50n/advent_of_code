import math

def read_data(filename: str):
    with open(filename, "r") as f:
        data = f.read().strip().split("\n")
    return list(zip(map(int, data[0].split()[1:]),
        map(int, data[1].split()[1:])))

def part1(data: list[tuple[int, int]]) -> int:
    res = 1
    for race in data:
        ways = 0
        for speed in range(race[0] + 1):
            final_position = (race[0] - speed) * speed
            if (final_position > race[1]):
                ways += 1
                
        res *= ways
    return res

def part2(time: int, dist: int) -> int:
    d = time**2 - 4 * dist
    assert d > 0 # assert we have solutions
    x1 = (time - math.sqrt(d)) / 2
    x2 = (time + math.sqrt(d)) / 2
    return math.floor(x2) - math.ceil(x1) + 1


if __name__ == "__main__":
    test_data = read_data('test_input')
    data = read_data('input')
    assert(part1(test_data) == 288)
    print(part1(data))

    time_t = int(''.join(map(lambda x: str(x[0]), test_data)))
    dist_t = int(''.join(map(lambda x: str(x[1]), test_data)))
    assert part2(time_t, dist_t) == 71503


    time = int(''.join(map(lambda x: str(x[0]), data)))
    dist = int(''.join(map(lambda x: str(x[1]), data)))
    print(part2(time, dist))

