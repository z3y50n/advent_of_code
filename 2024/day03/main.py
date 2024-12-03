import re


def read_data(filename):
    with open(filename, "r") as f:
        data = f.read().strip()
    return data


def part1(instructions: str) -> int:
    mults: list[str] = re.findall(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)", instructions)
    return sum(int(a) * int(b) for a, b in mults)


def part2(instructions: str) -> int:
    matches = re.findall(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)|(do)\(\)|(don't)\(\)", instructions)
    enabled = True
    res = 0
    for match in matches:
        if 'do' in match:
            enabled = True
        elif "don't" in match:
            enabled = False
        else:
            if enabled:
                res += int(match[0]) * int(match[1])
    return res


if __name__ == "__main__":
    test_instructions1 = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'
    instructions = read_data("input")

    assert part1(test_instructions1) == 161
    print(part1(instructions))

    test_instructions2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    assert part2(test_instructions2) == 48
    print(part2(instructions))
