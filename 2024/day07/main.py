def read_data(filename):
    with open(filename, "r") as f:
        data = f.read().strip().split("\n")

    ret = []
    for eq in data:
        test, rest = eq.split(": ")
        ret.append((int(test), list(map(int, rest.split(" ")))))
    return ret


def part1(equations: list[tuple[int, list[int]]]) -> int:
    return sum(eq[0] for eq in equations if is_valid(eq[0], eq[1]))


def is_valid(test: int, nums: list[int], r: int = 0) -> bool:
    if len(nums) == 0:
        return test == r

    return is_valid(test, nums[1:], r + nums[0]) or is_valid(
        test, nums[1:], r * nums[0]
    )


def part2(equations: list[tuple[int, list[int]]]) -> int:
    return sum(eq[0] for eq in equations if is_valid2(eq[0], eq[1]))


def is_valid2(test: int, nums: list[int], r: int = 0) -> bool:
    if len(nums) == 0:
        return test == r

    concat = int(f"{r}{nums[0]}")
    return (
        is_valid2(test, nums[1:], r + nums[0])
        or is_valid2(test, nums[1:], r * nums[0])
        or is_valid2(test, nums[1:], concat)
    )


if __name__ == "__main__":
    t_equations = read_data("test_input")
    equations = read_data("input")

    assert part1(t_equations) == 3749
    print(part1(equations))

    assert part2(t_equations) == 11387
    # takes a few seconds
    print(part2(equations))
