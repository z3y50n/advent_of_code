def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read().strip().split("\n")
    return data
    # return list(map(lambda x: x.split(','), data))

pairs = read_data('input.txt')
t_pairs = read_data('test_input.txt')

def part1(pairs):
    total = 0
    for pair in pairs:
        pair1, pair2 = pair.split(',')
        l11, l12 = map(int, pair1.split('-'))
        l21, l22 = map(int, pair2.split('-'))
        if (l11 >= l21 and l12 <= l22) or (l11 <= l21 and l12 >= l22):
            total += 1
    return total

assert part1(t_pairs) == 2
print(part1(pairs))

def part2(pairs):
    total = 0
    for pair in pairs:
        pair1, pair2 = pair.split(',')
        l11, l12 = map(int, pair1.split('-'))
        l21, l22 = map(int, pair2.split('-'))
        if (l11 >= l21 and l11 <= l22) or (l12 >= l21 and l12 <= l22):
            total += 1
        elif (l11 >= l21 and l12 <= l22) or (l11 <= l21 and l12 >= l22):
            total += 1
    return total

assert part2(t_pairs) == 4
print(part2(pairs))