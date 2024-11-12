type Maps = list[list[tuple[int, int, int]]]


def read_data(filename: str):
    with open(filename, "r") as f:
        data = f.read().strip().split("\n")
    seeds = list(map(int, data[0].split(": ")[1].split()))
    maps: Maps = []
    for row in data[1:]:
        if len(row) == 0:
            continue
        if "map:" in row:
            maps.append([])
        else:
            maps[-1].append(tuple(map(int, row.split())))
    return seeds, maps


def part1(seeds: list[int], maps: Maps) -> int:
    return min(map(lambda seed: find_seed_location(seed, maps), seeds))


def find_seed_location(seed: int, maps: Maps) -> int:
    current = seed
    for step in maps:
        current = convert(current, step)
    return current


def convert(current: int, step: list[tuple[int, int, int]]) -> int:
    for r in step:
        target, source, length = r
        if current >= source and current < source + length:
            diff = current - source
            return target + diff
    return current


def part2(seeds: list[int], maps: Maps):
    seed_ranges = list(map(lambda x: (x[0], x[0] + x[1]), zip(seeds[::2], seeds[1::2])))
    return min(
        map(
            lambda seed_range: find_min_seed_range_location(seed_range, maps),
            seed_ranges,
        )
    )


def find_min_seed_range_location(seed_range: tuple[int, int], maps: Maps) -> int:
    current_ranges = [seed_range]
    for m in maps:
        current_ranges = convert_ranges(current_ranges, m)

    return min(r[0] for r in current_ranges)


def convert_ranges(
    ranges: list[tuple[int, int]], step: list[tuple[int, int, int]]
) -> list[tuple[int, int]]:
    new_ranges = []
    for r in ranges:
        new_ranges.extend(convert_range(r, step))
    return new_ranges


def convert_range(
    r: tuple[int, int], step: list[tuple[int, int, int]]
) -> list[tuple[int, int]]:
    converted = []
    remaining = [r]
    for move in step:
        target, source, length = move
        not_converted = []
        for r_start, r_end in remaining:
            before = (r_start, min(source, r_end))
            inter = (max(r_start, source), min(r_end, source + length))
            after = (max(r_start, source + length), r_end)

            if before[1] > before[0]:
                not_converted.append(before)
            if inter[1] > inter[0]:
                converted.append(
                    (target + inter[0] - source, target + inter[1] - source)
                )
            if after[1] > after[0]:
                not_converted.append(after)

        remaining = not_converted
    return converted + remaining


if __name__ == "__main__":
    seeds_t, maps_t = read_data("test_input")
    seeds, maps = read_data("input")
    assert part1(seeds_t, maps_t) == 35
    print(part1(seeds, maps))

    assert part2(seeds_t, maps_t) == 46
    print(part2(seeds, maps))
