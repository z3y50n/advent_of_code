from tqdm import tqdm

tcups = [int(d) for d in str(389125467)]
cups = [int(d) for d in str(476138259)]

N_ROUND = 100

def get_pick(cups, cur_idx):
    pick = []
    for _ in range(3):
        idx = cur_idx + 1
        if idx >= len(cups): idx = 0
        pick.append(cups.pop(idx))
    return pick


def insert_pick(cups, pick, dest):
    idx = cups.index(dest)
    for i, d in enumerate(pick):
        cups.insert(idx+i+1, d)

# PART 1
def part1(cups):
    cur_idx = 0
    for _ in range(N_ROUND):
        cur_d = cups[cur_idx]

        pick = get_pick(cups, cur_idx)
        
        dest = cur_d - 1 if cur_d > 1 else 9
        while dest in pick:
            dest -= 1
            if dest <= 0: dest = 9

        insert_pick(cups, pick, dest)
        cur_idx = (cups.index(cur_d) + 1) % len(cups)
    one_idx = cups.index(1)
    return cups[one_idx+1:] + cups[:one_idx]

tres = part1(tcups.copy())
res = part1(cups.copy())
assert "".join(str(d) for d in tres) == "67384529"
print("".join(str(d) for d in res))

# PART 2 (Using a Linked List)
N_ROUND = 10000000
tcups += list(range(10, 1000001))
cups += list(range(10, 1000001))

def get_linked_cups(cups):
    linked_cups = {}
    for i, cup in enumerate(cups):
        linked_cups[cup] = cups[(i+1) % (len(cups))]
    return linked_cups

def get_pick2(lcups, cur_d):
    pick = []
    for _ in range(3):
        n = lcups[cur_d]
        pick.append(n)
        lcups[cur_d] = lcups[n]
    return pick

def insert_pick2(lcups, pick, dest):
    temp = lcups[dest]
    lcups[dest] = pick[0]
    lcups[pick[0]] = pick[1]
    lcups[pick[1]] = pick[2]
    lcups[pick[2]] = temp

def part2(cups):
    cur_d = cups[0]
    lcups = get_linked_cups(cups)
    for _ in tqdm(range(N_ROUND)):
        pick = get_pick2(lcups, cur_d)
        
        dest = cur_d - 1 if cur_d > 1 else 1000000
        while dest in pick:
            dest -= 1
            if dest <= 0: dest = 1000000

        insert_pick2(lcups, pick, dest)
        cur_d = lcups[cur_d]
    return lcups[1], lcups[lcups[1]]
    

tres = part2(tcups) # (934001, 159792)
res = part2(cups)
print(res[0] * res[1])
