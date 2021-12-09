def read_data(filename):
    with open(filename, "r") as f:
        data = f.read().strip().split("\n")

    patterns = [l.split(" | ")[0].split(" ") for l in data]
    outputs = [l.split(" | ")[1].split(" ") for l in data]
    return patterns, outputs


t_patterns, t_outputs = read_data("test_input.txt")
patterns, outputs = read_data("input.txt")


def part1(outputs):
    ret = 0
    for segment in outputs:
        for digit in segment:
            if len(digit) in (2, 3, 4, 7):
                ret += 1
    return ret


assert part1(t_outputs) == 26
print(part1(outputs))


def remaining_digits(n1, n2):
    return list(set(n1).symmetric_difference(set(n2)))


def find_number(numbers, d):
    for i, n in enumerate(numbers):
        if len(remaining_digits(n, d)) == 0:
            return i


def part2(patterns, outputs):
    s = 0
    for pattern, output in zip(patterns, outputs):
        numbers = [""] * 10
        p = sorted(pattern, key=len)
        numbers[1] = p[0]
        numbers[7] = p[1]
        numbers[4] = p[2]
        numbers[8] = p[9]
        for ttf in p[3:6]:
            if len(remaining_digits(ttf, numbers[1])) == 3:
                numbers[3] = ttf
            else:
                if len(remaining_digits(ttf, numbers[4])) == 3:
                    numbers[5] = ttf
                else:
                    numbers[2] = ttf
        for zsn in p[6:9]:
            if len(remaining_digits(zsn, numbers[3] + numbers[4] + numbers[7])) == 0:
                numbers[9] = zsn
            else:
                if len(remaining_digits(zsn, numbers[5])) == 1:
                    numbers[6] = zsn
                else:
                    numbers[0] = zsn
        for i, d in enumerate(output):
            s += find_number(numbers, d) * 10 ** (len(output) - 1 - i)
    return s


assert part2(t_patterns, t_outputs) == 61229
print(part2(patterns, outputs))
