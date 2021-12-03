from collections import Counter


def read_data(filename):
    with open(filename, "r") as f:
        data = f.read().strip().split("\n")
    return data


data = read_data("input.txt")
test_data = read_data("test_input.txt")

# PART 1
def part1(data):
    blocks = ["".join([num[i] for num in data]) for i in range(len(data[0]))]
    gamma = []
    epsilon = []
    for block in blocks:
        c = Counter(block).most_common(2)
        g_bit = c[0][0]
        e_bit = c[1][0]
        gamma.append(g_bit)
        epsilon.append(e_bit)
    gamma = "".join(gamma)
    epsilon = "".join(epsilon)

    return int(gamma, 2) * int(epsilon, 2)


assert part1(test_data) == 198
print(part1(data))

# PART 2
def extract(rating, mask):
    idx = 0
    while len(rating) > 1:
        new = rating.copy()
        bits = [val[idx] for val in rating]
        c = Counter(bits)
        bit = c.most_common(2)[mask][0]
        if c["1"] == c["0"]:
            bit = str(int(not mask))

        for val in rating:
            if val[idx] != bit:
                new.remove(val)
        rating = new.copy()
        idx += 1
    return rating[0]


def part2(data):
    ox_rating = extract(data.copy(), 0)
    co2_rating = extract(data.copy(), 1)
    return int(ox_rating, 2) * int(co2_rating, 2)


assert part2(test_data) == 230
print(part2(data))
