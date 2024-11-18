type Springs = list[tuple[str, list[int]]]


def read_data(filename) -> Springs:
    with open(filename, "r") as f:
        data = f.read().strip().split("\n")

    # add extra dot at the end so we can handle last springs
    return [(row.split()[0], list(map(int, row.split()[1].split(",")))) for row in data]


def part1(springs: Springs) -> int:
    return sum(map(get_spring_arrangements, springs))

def part2(springs: Springs) -> int:
    expanded = [('?'.join([s[0]] * 5), s[1] * 5) for s in springs]
    return sum(map(get_spring_arrangements, expanded))


def get_spring_arrangements(spring: tuple[str, list[int]]) -> int:
    springs, groups = spring
    springs = springs + '.'

    dfs = {}
    def count_springs(spring_idx: int, group_idx: int, r=0) -> int:
        if (spring_idx, group_idx) in dfs:
            return dfs[(spring_idx, group_idx)]
        # if we reach the end of string, check if we have placed all springs
        if spring_idx == len(springs):
            r += group_idx == len(groups)
            dfs[(spring_idx, group_idx)] = r
            return r
        if springs[spring_idx] in ".?":
            r += count_springs(spring_idx + 1, group_idx)
        try:
            n = spring_idx + groups[group_idx]
            if "." not in springs[spring_idx:n] and springs[n] != '#':
                r += count_springs(n+1, group_idx+1)
        except IndexError:
            pass
        dfs[(spring_idx, group_idx)] = r
        return r

    res =  count_springs(0, 0)
    return res


if __name__ == "__main__":
    test_springs = read_data("test_input")
    springs = read_data("input")
    assert part1(test_springs) == 21
    print(part1(springs))
    assert part2(test_springs) == 525152
    print(part2(springs))
