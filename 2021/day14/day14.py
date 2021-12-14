from collections import defaultdict, Counter


def read_data(filename):
    with open(filename, "r") as f:
        template, pairs = f.read().strip().split("\n\n")

    pairs = dict([pair.split(" -> ") for pair in pairs.split("\n")])

    return template, pairs


t_template, t_pairs = read_data("test_input.txt")
template, pairs = read_data("input.txt")


# PART 1 (Slow Using lists)
def part1(template, pairs, steps):
    polymer = []
    cur_template = template
    for step in range(steps):
        for i in range(len(cur_template) - 1):
            polymer.append(cur_template[i])
            pair = cur_template[i : i + 2]
            polymer.append(pairs[pair])
        polymer.append(cur_template[-1])
        cur_template = "".join(polymer)
        polymer = []
    c = Counter(cur_template)
    big = c.most_common(1)[0][1]
    small = c.most_common()[-1][1]
    return big - small


assert part1(t_template, t_pairs, 10) == 1588
print(part1(template, pairs, 10))

# PART 2 Fast with dictionaries
def part2(template, pairs, steps):
    # Initialize pair counts
    pair_counts = defaultdict(int)
    letter_counts = defaultdict(int)
    for i in range(len(template) - 1):
        pair_counts[template[i : i + 2]] += 1
        letter_counts[template[i]] += 1
    letter_counts[template[-1]] += 1

    for step in range(steps):
        new_counts = defaultdict(int)
        for pair in pair_counts:
            first = pair[0]
            second = pair[1]
            new_letter = pairs[pair]
            pair_count = pair_counts[pair]
            new_counts[first + new_letter] += pair_count
            new_counts[new_letter + second] += pair_count
            letter_counts[new_letter] += pair_count
        pair_counts = new_counts

    big = max(letter_counts.values())
    small = min(letter_counts.values())
    return big - small


assert part2(t_template, t_pairs, 40) == 2188189693529
print(part2(template, pairs, 40))
