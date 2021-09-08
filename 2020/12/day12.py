def read_data(filename):
    with open(filename, "r") as f:
        data = f.read().split("\n")[:-1]
    instructions = [(inst[0], int(inst[1:])) for inst in data]
    return instructions

instructions = read_data("day12.txt")
#instructions = [('F', 10), ('N', 3), ('F', 7), ('R', 90), ('F', 11)]
print(instructions)

# PART 1
rotations = {90: 1, 180: 2, 270:3}
transitions = ['E', 'S', 'W', 'N']

def part_1(instructions):
    x = 0
    y = 0
    direction = 'E'
    for mv in instructions:
        if mv[0] == 'E' or (mv[0] == 'F' and direction=='E'):
            x += mv[1]
        elif mv[0] == 'S' or (mv[0] == 'F' and direction=='S'):
            y -= mv[1]
        elif mv[0] == 'W' or (mv[0] == 'F' and direction=='W'):
            x -= mv[1]
        elif mv[0] == 'N' or (mv[0] == 'F' and direction=='N'):
            y += mv[1]
        elif mv[0] == 'R':
            idx = transitions.index(direction)
            direction = transitions[(idx + rotations[mv[1]])%4]
        elif mv[0] == 'L':
            idx = transitions.index(direction)
            direction = transitions[(idx - rotations[mv[1]])%4]
    return (x, y)

pos = part_1(instructions)
print(pos)
print(abs(pos[0])+abs(pos[1]))

# PART 2
def part_2(instructions):
    s_x = 0
    s_y = 0
    w_x = 10
    w_y = 1
    for mv in instructions:
        if mv[0] == 'E':
            w_x += mv[1]
        elif mv[0] == 'S':
            w_y -= mv[1]
        elif mv[0] == 'W':
            w_x -= mv[1]
        elif mv[0] == 'N':
            w_y += mv[1]
        elif mv[0] == 'F':
            s_x += mv[1]*w_x
            s_y += mv[1]*w_y
        if mv[0] == 'L':
            mv = ('R', 360-mv[1])
        if mv[0] == 'R':
            if mv[1] == 90:
                w_x, w_y = w_y, -w_x
            elif mv[1] == 180:
                w_x, w_y = -w_x, -w_y
            elif mv[1] == 270:
                w_x, w_y = -w_y, w_x
    return s_x, s_y

pos = part_2(instructions)
print(pos)
print(abs(pos[0]) + abs(pos[1]))

