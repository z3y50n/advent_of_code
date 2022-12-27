POWER_CYCLES = [20, 60, 100, 140, 180, 220]


def read_data(filename):
    with open(filename, "r") as f:
        return list(map(lambda x: x.split(), f.read().strip().split("\n")))


t_instructions = read_data("test_input.txt")
instructions = read_data("input.txt")


class CPU:
    def __init__(self, instructions):
        self.pc = 0
        self.add = 0
        self.X = 1
        self.instructions = instructions

    def execute(self):
        if self.add == 1:
            instruction = self.fetchInstruction()
            self.X += int(instruction[1])
            self.pc += 1
            self.add = 0
        else:
            instruction = self.fetchInstruction()
            if instruction[0] == "noop":
                self.pc += 1
            elif instruction[0] == "addx":
                self.add = 1

    def fetchInstruction(self):
        return self.instructions[self.pc]

    def print_state(self):
        print("***")
        print(self.pc)
        print(self.instructions[self.pc])
        print(self.add)
        print(self.X)
        print("***")


def part1(instructions):
    cpu = CPU(instructions)
    signal_strength = 0
    for cycle in range(1, 221):
        if cycle in POWER_CYCLES:
            signal_strength += cycle * cpu.X
        cpu.execute()
    return signal_strength


assert part1(t_instructions) == 13140
print(part1(instructions))


def part2(instructions):
    cpu = CPU(instructions)
    crt = [["0"] * 40 for _ in range(6)]
    step = 0
    for step in range(6*40):
        row = step // 40
        col = step % 40
        sprite_pos = cpu.X + row*40
        if sprite_pos-1 <= step <= sprite_pos+1:
            crt[row][col] = '#'
        else:
            crt[row][col] = '.'
        cpu.execute()
    for row in crt:
        print(''.join(row))

#part1(t_instructions)
part2(instructions)