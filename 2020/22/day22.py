def read_data(filename):
    with open(filename, "r") as f:
        data = f.read().strip().split("\n\n")

    player1 = list(map(int, data[0][10:].split("\n")))
    player2 = list(map(int, data[1][10:].split("\n")))
    return player1, player2

tplayer1, tplayer2 = read_data("testa.txt")
player1, player2 = read_data("day22.txt")

# PART 1
def part1(player1, player2):
    while player1 and player2:
        top1 = player1.pop(0)
        top2 = player2.pop(0)
        if top1 > top2:
            player1 += [top1, top2]
        else:
            player2 += [top2, top1]

    winner = 1 if player1 else 2
    win = player1 if player1 else player2
    pts = sum(num * (len(win)-i) for i, num in enumerate(win))
    print(f"Player {winner} wins with deck {win}")
    return pts

assert part1(tplayer1.copy(), tplayer2.copy()) == 306

print(f"Part1 points: {part1(player1.copy(), player2.copy())}")

# PART 2
def part2(player1, player2):
    memory = []
    while player1 and player2:
        if (player1, player2) in memory:
            return 1
        memory.append((player1.copy(), player2.copy()))
        top1 = player1.pop(0)
        top2 = player2.pop(0)
        if len(player1) >= top1 and len(player2) >= top2:
            winner = part2(player1[:top1], player2[:top2])
            if winner == 1:
                player1 += [top1, top2]
            else:
                player2 += [top2, top1]
        else:
            if top1 > top2:
                player1 += [top1, top2]
                winner = 1
            else:
                player2 += [top2, top1]
                winner = 2
    return 1 if player1 else 2

twinner = part2(tplayer1, tplayer2)
tplayer = tplayer1 if tplayer1 else tplayer2
tpts = sum(num * (len(tplayer)-i) for i, num in enumerate(tplayer))
assert tpts == 291

winner = part2(player1, player2)
player = player1 if player1 else player2
pts = sum(num * (len(player)-i) for i, num in enumerate(player))
print(f"Player {winner} wins with deck {player}")
print(f"Part2 points: {pts}")
