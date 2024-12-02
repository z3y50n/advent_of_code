def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read().strip()
    return data.split(',')


def part1(seq: list[str]) -> int:
    return sum(map(hash, seq))


def hash(step: str) -> int:
    h = 0
    for char in step:
        h += ord(char)
        h *= 17
        h %= 256
    return h


def part2(seq: list[str]) -> int:
    boxes: list[list[tuple[str, int]]] = [[] for _ in range(256)]

    for step in seq:
        if '-' in step:
            box_idx = hash(step[:-1])
            label = step[:-1]
            for i, s in enumerate(boxes[box_idx]):
                if s[0] == label:
                    boxes[box_idx].pop(i)
                    break
        else:
            box_idx = hash(step[:-2])
            label = step[:-2]
            lens = int(step[-1])
            found = False
            for i, s in enumerate(boxes[box_idx]):
                if s[0] == label:
                    boxes[box_idx][i] = (label, lens)
                    found = True
                    break
            if not found:
                boxes[box_idx].append((label, lens))
    res = 0
    for i, box in enumerate(boxes):
        for j, s in enumerate(box):
            res += (i+1) * (j+1) * s[1]
    return res


if __name__ == "__main__":
    seq = read_data('input')
    test_seq = read_data('test_input')
    assert part1(test_seq) == 1320
    print(part1(seq))
    assert part2(test_seq) == 145
    print(part2(seq))