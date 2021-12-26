import math
from collections import deque
from itertools import permutations


def read_data(filename):
    with open(filename, "r") as f:
        data = f.read().strip().split("\n")
    return list(map(list, data))


numbers = read_data("input.txt")
t_numbers = read_data("test_input.txt")


def snail_add(first, second):
    number = ["["] + first + [","] + second + ["]"]
    res = snail_reduce(number)
    return res


def snail_reduce(number):
    explode_idx = find_explode(number)
    split_idx = find_split(number)

    while explode_idx != -1 or split_idx != -1:
        if explode_idx != -1:
            number = explode(number, explode_idx)
        elif split_idx != -1:
            number = split(number, split_idx)
        explode_idx = find_explode(number)
        split_idx = find_split(number)
    return number


def find_explode(number):
    end_cnt = 0
    for i, c in enumerate(number):
        if c == "[":
            start = i
            end_cnt += 1
        elif c == "]":
            end_cnt -= 1
        if end_cnt == 5:
            return start + 1
    return -1


def find_split(number):
    for i, c in enumerate(number[:-1]):
        if c.isdigit() and int(c) >= 10:
            return i
    return -1


def explode(number, idx):
    pair = "".join(number[idx : idx + 1 + number[idx + 1 :].index("]")])
    left, right = pair.split(",")
    left_idx = -1
    right_idx = -1
    left_val = None
    right_val = None
    for i, c in enumerate(number):
        if c.isdigit() and i < idx:
            left_idx = i
            left_val = int(c)
        if c.isdigit() and i > idx + 1 + number[idx + 1 :].index("]"):
            right_idx = i
            right_val = int(c)
            break

    if left_idx != -1:
        number[left_idx] = str(left_val + int(left))
    if right_idx != -1:
        number[right_idx] = str(right_val + int(right))

    for i in range(idx, idx + 2 + number[idx + 1 :].index("]")):
        number.pop(idx)
    number[idx - 1] = "0"
    return number


def split(number, idx):
    left = int(number[idx]) // 2
    right = math.ceil(int(number[idx]) / 2)
    number[idx] = "["
    number.insert(idx + 1, str(left))
    number.insert(idx + 2, ",")
    number.insert(idx + 3, str(right))
    number.insert(idx + 4, "]")
    return number


def magnitude(number):
    stack = deque()
    for c in number:
        stack.append(c)
        if c == "]":
            v = stack.pop()
            pair = []
            while v != "[":
                pair.append(v)
                v = stack.pop()
            stack.append(2 * int(pair[1]) + 3 * int(pair[3]))
    return stack[0]


def part1(numbers):
    first = numbers[0]
    for second in numbers[1:]:
        first = snail_add(first, second)
    return magnitude(first)


assert part1(t_numbers) == 4140
print(part1(numbers))


def part2(numbers):
    max_magnitute = 0
    for perm in permutations(numbers, 2):
        n = snail_add(perm[0], perm[1])
        mag = magnitude(n)
        if mag > max_magnitute:
            max_magnitute = mag
    return max_magnitute


assert part2(t_numbers) == 3993
print(part2(numbers))
