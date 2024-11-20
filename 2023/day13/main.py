from math import log2


def read_data(filename: str):
    with open(filename, "r") as f:
        data = f.read().strip().split("\n\n")

    return [pattern.split("\n") for pattern in data]


def print_pattern(pattern: list[str]):
    for row in pattern:
        print(row)
    print("\n")


def part1(patterns: list[list[str]]) -> int:
    return sum(map(find_mirrors, patterns))


def part2(patterns: list[list[str]]) -> int:
    res = 0
    for pattern in patterns:
        c = get_column_numbers(pattern)
        r = get_row_numbers(pattern)
        res += find_mirror_index_part2(c) + 100 * find_mirror_index_part2(r)
    return res


def find_mirrors(pattern: list[str]) -> int:
    c = get_column_numbers(pattern)
    r = get_row_numbers(pattern)

    return find_mirror_index(c) + 100 * find_mirror_index(r)


def get_column_numbers(pattern: list[str]) -> list[int]:
    return [
        int("".join(["0" if row[j] == "." else "1" for row in pattern]), 2)
        for j in range(len(pattern[0]))
    ]


def get_row_numbers(pattern: list[str]) -> list[int]:
    return [int(row.replace(".", "0").replace("#", "1"), 2) for row in pattern]


def find_mirror_index(numbers: list[int]) -> int:
    for i in range(len(numbers) - 1):
        if numbers[i] == numbers[i + 1]:
            j = 1
            isMiror = True
            while i - j >= 0 and i + j + 1 < len(numbers):
                if numbers[i - j] != numbers[i + j + 1]:
                    isMiror = False
                    break
                j += 1
            if isMiror:
                return i + 1
    return 0


def get_found_smudge(a, b):
    return a != b and log2(abs(a - b)).is_integer()


def find_mirror_index_part2(numbers: list[int]) -> int:
    for i in range(len(numbers) - 1):
        if (
            numbers[i] == numbers[i + 1]
            or log2(abs(numbers[i] - numbers[i + 1])).is_integer()
        ):
            found_smudge = get_found_smudge(numbers[i], numbers[i + 1])
            j = 1
            isMiror = True
            while i - j >= 0 and i + j + 1 < len(numbers):
                if (
                    numbers[i - j] != numbers[i + j + 1]
                    and (found_smudge or not log2(abs(numbers[i - j] - numbers[i + j + 1])).is_integer())
                ):
                    isMiror = False
                    break
                found_smudge = found_smudge or get_found_smudge(numbers[i - j], numbers[i + j + 1])
                j += 1
            if isMiror and found_smudge:
                return i + 1
    return 0


if __name__ == "__main__":
    test_patterns = read_data("test_input")
    patterns = read_data("input")
    assert part1(test_patterns) == 405
    print(part1(patterns))

    assert part2(test_patterns) == 400
    print(part2(patterns))
