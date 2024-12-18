from collections import deque
from dataclasses import dataclass


def read_data(filename):
    with open(filename, "r") as f:
        return f.read().strip()


def part1(disk: str) -> int:
    spaces: deque[int] = deque([])
    files: deque[tuple[int, int]] = deque([])
    fid = 0
    pos = 0
    for i, n in enumerate(disk):
        number = int(n)
        if i % 2 == 0:
            for c in range(number):
                files.append((pos + c, fid))
            fid += 1
        else:
            for c in range(number):
                spaces.append(pos + c)
        pos += number

    checksum = 0
    while files[-1][0] > spaces[0]:
        if files[0][0] < spaces[0]:
            pos, fid = files.popleft()
            checksum += pos * fid
        else:
            _, fid = files.pop()
            pos = spaces.popleft()
            checksum += pos * fid
    # There might be some leftover files
    for pos, fid in files:
        checksum += pos * fid
    return checksum


@dataclass
class Space:
    pos: int
    size: int


@dataclass
class File:
    pos: int
    size: int
    fid: int


def part2(disk: str) -> int:
    spaces: list[Space] = []
    files: list[File] = []
    fid = 0
    pos = 0
    for i, n in enumerate(disk):
        number = int(n)
        if i % 2 == 0:
            files.append(File(pos, number, fid))
            fid += 1
        else:
            spaces.append(Space(pos, number))
        pos += number

    for file in reversed(files):
        space_i = 0
        while spaces[space_i].pos < file.pos:
            space = spaces[space_i]
            if space.size > file.size:
                file.pos, space.pos = space.pos, space.pos + file.size
                space.size -= file.size
                break
            elif space.size == file.size:
                space.size = 0
                file.pos = space.pos
                break
            space_i += 1

    checksum = 0
    for file in files:
        for i in range(file.pos, file.pos+file.size):
            checksum += i * file.fid
    return checksum



if __name__ == "__main__":
    test_disk = read_data("test_input.txt")
    disk = read_data("input.txt")

    assert part1(test_disk) == 1928
    print(part1(disk))

    assert part2(test_disk) == 2858
    # takes a few seconds
    print(part2(disk))
