import re


def read_data(filename: str):
    with open(filename, "r") as f:
        data = f.read().strip().split("\n\n")

    machines = []
    for m in data:
        A, B, G = m.split("\n")
        a1, a2 = map(int, re.findall(r"(\d+)", A))
        b1, b2 = map(int, re.findall(r"(\d+)", B))
        c1, c2 = map(int, re.findall(r"(\d+)", G))
        machines.append(
            {
                "a1": a1,
                "b1": b1,
                "a2": a2,
                "b2": b2,
                "c1": c1,
                "c2": c2,
            }
        )
    return machines


def part1(machines: list[dict[str, int]]) -> int:
    ret = 0
    for m in machines:
        a1, a2 = m["a1"], m["a2"]
        b1, b2 = m["b1"], m["b2"]
        c1, c2 = m["c1"], m["c2"]
        X = (b2 * c1 - b1 * c2) / (b2 * a1 - b1 * a2)
        Y = (c1 * (b2 * a1 - b1 * a2) - a1 * (b2 * c1 - b1 * c2) ) / (
            b1 * (b2 * a1 - b1 * a2)
        )
        if X.is_integer() and Y.is_integer():
            ret += int(X*3 + Y)
    return ret


def part2(machines: list[dict[str, int]]) -> int:
    ret = 0
    for m in machines:
        a1, a2 = m["a1"], m["a2"]
        b1, b2 = m["b1"], m["b2"]
        c1, c2 = m["c1"] + 10000000000000, m["c2"] + 10000000000000
        X = (b2 * c1 - b1 * c2) / (b2 * a1 - b1 * a2)
        Y = (c1 * (b2 * a1 - b1 * a2) - a1 * (b2 * c1 - b1 * c2) ) / (
            b1 * (b2 * a1 - b1 * a2)
        )
        if X.is_integer() and Y.is_integer():
            # Y is minus due to chat gpt not knowing math
            ret += int(X*3 + Y)
    return ret


if __name__ == "__main__":
    machines = read_data("input.txt")
    test_machines = read_data("test_input.txt")
    assert part1(test_machines) == 480
    print(part1(machines))

    print(part2(machines))

