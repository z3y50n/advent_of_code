def read_data(filename):
    with open(filename, "r") as f:
        data = f.read().strip().split()
    return data


# `solution` is infinitely faster, but keep this for completion
def part1(stones: list[str]):
    s = stones.copy()
    for _ in range(25):
        new_s = []
        for stone in s:
            if stone == "0":
                new_s.append("1")
            elif len(stone) % 2 == 0:
                new_s.append(stone[: len(stone) // 2])
                second = stone[len(stone) // 2 :].lstrip("0")
                if second == "":
                    new_s.append("0")
                else:
                    new_s.append(second)
            else:
                new_s.append(str(int(stone) * 2024))
        s = new_s.copy()
    return len(s)


def solution(stones: list[str], blinks: int) -> int:
    r = 0
    for stone in stones:
        r += solve(stone, blinks)
    return r


cache = {}
def solve(stone: str, blink: int) -> int:
    if (stone, blink) in cache:
        return cache[(stone, blink)]
    r = 0
    if blink == 1:
        if stone == "0":
            r = 1
        elif len(stone) % 2 == 0:
            r = 2
        else:
            r = 1
    else:
        if stone == "0":
            r += solve("1", blink - 1)
        elif len(stone) % 2 == 0:
            r += solve(stone[: len(stone) // 2], blink - 1)
            second = stone[len(stone) // 2 :].lstrip("0")
            if second == "":
                r += solve("0", blink - 1)
            else:
                r += solve(second, blink - 1)
        else:
            r += solve(str(int(stone) * 2024), blink - 1)
    cache[(stone, blink)] = r
    return r


if __name__ == "__main__":
    test_stones = read_data("test_input.txt")
    stones = read_data("input.txt")

    assert solution(test_stones, 25) == 55312
    print(solution(stones, 25))
    print(solution(stones, 75))
