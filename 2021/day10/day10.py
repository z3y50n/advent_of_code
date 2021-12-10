from collections import deque, defaultdict
import statistics


def read_data(filename):
    with open(filename, "r") as f:
        data = f.read().strip().split("\n")
    return data


t_lines = read_data("test_input.txt")
lines = read_data("input.txt")

POINTS1 = {")": 3, "]": 57, "}": 1197, ">": 25137}
POINTS2 = {")": 1, "]": 2, "}": 3, ">": 4}
PAIRS = {"(": ")", "[": "]", "{": "}", "<": ">"}


def part1(lines):
    counts = defaultdict(int)
    good_lines = []
    for line in lines:
        stack = deque()
        for c in line:
            if c in ("(", "[", "{", "<"):
                stack.append(c)
            else:
                pair = stack.pop()
                if PAIRS[pair] != c:
                    counts[c] += 1
                    break
        else:
            good_lines.append(line)
    s = sum(POINTS1[c] * n for c, n in counts.items())
    return s, good_lines


t_s, t_glines = part1(t_lines)
assert t_s == 26397
s, glines = part1(lines)
print(s)


def part2(glines):
    scores = [0] * len(glines)
    for i, line in enumerate(glines):
        stack = deque()
        t_add = []
        # Find remaining characters to close
        for c in line:
            if c in ("(", "[", "{", "<"):
                stack.append(c)
            else:
                pair = stack.pop()
        # Find characters to add at the end
        while len(stack) != 0:
            pair = stack.pop()
            t_add.append(PAIRS[pair])

        # calculate score
        for c in t_add:
            scores[i] = 5 * scores[i] + POINTS2[c]

    # Return median value
    return statistics.median(scores)


assert part2(t_glines) == 288957
print(part2(glines))
