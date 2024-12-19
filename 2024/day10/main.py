def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read().strip().split('\n')
    return data


def solution(trailhead: list[str], part2=False) -> int:
    H = len(trailhead)
    W = len(trailhead[0])
    trail_score = 0
    for i in range(H):
        for j in range(W):
            if trailhead[i][j] == '0':
                if part2:
                    trail_score += find_trails2(trailhead, i, j)
                else:
                    trail_score += find_trails(trailhead, i, j)
    return trail_score

steps = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def find_trails(trailhead: list[str], start_i: int, start_j: int) -> int:
    H = len(trailhead)
    W = len(trailhead[0])
    stack = [(start_i, start_j)]
    found: set[tuple[int, int]] = set()
    score = 0
    while len(stack):
        pos = stack.pop()
        if trailhead[pos[0]][pos[1]] == '9' and pos not in found:
            found.add(pos)
            score += 1
        for step in steps:
            new_pos = (pos[0] + step[0], pos[1] + step[1])
            if 0 <= new_pos[0] < H and 0 <= new_pos[1] < W:
                cur_val = int(trailhead[pos[0]][pos[1]])
                next_val = int(trailhead[new_pos[0]][new_pos[1]])
                if next_val == cur_val + 1:
                    stack.append(new_pos)
    return score


def find_trails2(trailhead: list[str], start_i: int, start_j: int) -> int:
    H = len(trailhead)
    W = len(trailhead[0])
    stack = [(start_i, start_j)]
    score = 0
    while len(stack):
        pos = stack.pop()
        if trailhead[pos[0]][pos[1]] == '9':
            score += 1
        for step in steps:
            new_pos = (pos[0] + step[0], pos[1] + step[1])
            if 0 <= new_pos[0] < H and 0 <= new_pos[1] < W:
                cur_val = int(trailhead[pos[0]][pos[1]])
                next_val = int(trailhead[new_pos[0]][new_pos[1]])
                if next_val == cur_val + 1:
                    stack.append(new_pos)
    return score

if __name__ == "__main__":
    test_trailhead = read_data('test_input.txt')
    trailhead = read_data('input.txt')

    assert solution(test_trailhead) == 36
    print(solution(trailhead))

    assert solution(test_trailhead, True) == 81
    print(solution(trailhead, True))

