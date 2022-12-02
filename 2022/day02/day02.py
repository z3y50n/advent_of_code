def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read().strip().split("\n")
    return list(map(lambda x: tuple(x.split()), data))

decrypt = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors',
}
scores = {'rock': 1, 'paper': 2, 'scissors': 3}
loses = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}

winnings = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}

strategy = read_data("input.txt")
t_strategy = read_data("test_input.txt")

def part1(strategy):
    score = 0
    for round in strategy:
        op = decrypt[round[0]]
        me = decrypt[round[1]]
        score += scores[me]
        if op == me:
            score += 3
        elif winnings[me] == op:
            score += 6
    return score

print(part1(strategy))

def part2(strategy):
    score = 0
    for round in strategy:
        op = decrypt[round[0]]
        if round[1] == 'X':
            score += scores[winnings[op]]
        elif round[1] == 'Y':
            score += 3 + scores[op]
        else:
            score += 6 + scores[loses[op]]
    return score

print(part2(strategy))

