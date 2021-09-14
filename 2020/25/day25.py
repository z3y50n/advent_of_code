tcard = 5764801
tdoor = 17807724

card = 12092626
door = 4707356

REMAINDER = 20201227

def find_loop_size(p_key, subject_number=7):
    value = 1
    loop_size = 0
    while value != p_key:
        value *= subject_number
        value = value % REMAINDER
        loop_size += 1
    return loop_size

tcard_loop = find_loop_size(tcard)
tdoor_loop = find_loop_size(tdoor)

card_loop = find_loop_size(card)
door_loop = find_loop_size(door)

def part1(p_key, loop_size):
    value = 1
    for i in range(loop_size):
        value *= p_key
        value %= REMAINDER
    return value

assert part1(tcard, tdoor_loop) == part1(tdoor, tcard_loop) == 14897079

print(part1(card, door_loop))
