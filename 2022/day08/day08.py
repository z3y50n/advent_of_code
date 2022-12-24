import math
from collections import defaultdict

def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read().strip().split('\n')
    return [list(map(int, list(d))) for d in data]

t_data = read_data('test_input.txt')
data = read_data('input.txt')

def part1(data):
    N = len(data)
    M = len(data[0])
    count = 2 * M + 2 * (N-2)
    canBeSeen = set()

    biggestPerColumn = [data[0][j] for j in range(M)]
    for i in range(1, N-1):
        biggestOfRow = data[i][0]
        for j in range(1, M-1):
            if data[i][j] > biggestOfRow or data[i][j] > biggestPerColumn[j]:
                biggestOfRow = max(biggestOfRow, data[i][j])
                biggestPerColumn[j] = max(biggestPerColumn[j], data[i][j])
                if (i, j) not in canBeSeen:
                    count += 1
                    canBeSeen.add((i, j))
    biggestPerColumn = [data[-1][j] for j in range(M)]
    for i in range(N-2, 0, -1):
        biggestOfRow = data[i][-1]
        for j in range(M-2, 0, -1):
            if data[i][j] > biggestOfRow or data[i][j] > biggestPerColumn[j]:
                biggestOfRow = max(biggestOfRow, data[i][j])
                biggestPerColumn[j] = max(biggestPerColumn[j], data[i][j])
                if (i, j) not in canBeSeen:
                    count += 1
                    canBeSeen.add((i, j))
    return count

tCount = part1(t_data)
assert tCount == 21
count = part1(data)
print(count)

def distOfRows(row):
    lastSeen = {row[0]: 0}
    distances = [0 for _ in range(len(row))]
    for i in range(1, len(row)):
        if row[i] <= row[i-1]:
            distances[i] = 1
        else:
            m = 0
            for j in range(row[i], 10):
                if j in lastSeen and lastSeen[j] > m:
                    m = lastSeen[j]
            distances[i] = i - m
        lastSeen[row[i]] = i
    return distances

def part2(data):
    N = len(data)
    M = len(data[0])
    distances = [[0] * M for _ in range(N)]
    for i in range(0, N):
        distances[i] = distOfRows(data[i])
        r = distOfRows(list(reversed(data[i])))
        distances[i] = [d * r for d, r in zip(distances[i], reversed(r))]
    for j in range(0, M):
        col = [data[i][j] for i in range(N)]
        n = distOfRows(col)
        r = list(reversed(distOfRows(list(reversed(col)))))
        for i in range(N):
            distances[i][j] *= n[i] * r[i]
    return max(map(max, distances))
        
assert part2(t_data) == 8
print(part2(data))