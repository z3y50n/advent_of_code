def get_data(filename: str):
    with open(filename, 'r') as f:
        data = f.read().strip().split("\n")
    return list(map(lambda x: list(map(int, x.split())), data))

def part1(oasis: list[list[int]]) -> int:
    res = 0
    for reading in oasis:
        res += find_reading_next_value(reading)
    return res

def find_reading_next_value(reading: list[int]) -> int:
    next_value = 0
    rows = [reading]
    while True:
        new_row = []
        for i in range(1, len(rows[-1])):
            new_row.append(rows[-1][i] - rows[-1][i-1])
        if not all(map(lambda x: x == 0, new_row)):
            rows.append(new_row)
        else:
            for i in range(len(rows)-1, -1, -1):
                next_value += rows[i][-1]
            break
    return next_value

def part2(oasis: list[list[int]]) -> int:
    res = 0
    for reading in oasis:
        res += find_reading_prev_value(reading)
    return res

def find_reading_prev_value(reading: list[int]) -> int:
    prev_value = 0
    rows = [reading]
    while True:
        new_row = []
        for i in range(1, len(rows[-1])):
            new_row.append(rows[-1][i] - rows[-1][i-1])
        if not all(map(lambda x: x == 0, new_row)):
            rows.append(new_row)
        else:
            for i in range(len(rows)-1, -1, -1):
                prev_value = rows[i][0] - prev_value
            break
    return prev_value

if __name__ == "__main__":
    test_oasis = get_data('test_input')
    oasis = get_data('input')
    # print(test_oasis)
    assert part1(test_oasis) == 114
    print(part1(oasis))
    assert part2(test_oasis) == 2
    print(part2(oasis))