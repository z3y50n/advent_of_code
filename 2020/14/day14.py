def read_instructions(filename):
    with open(filename, "r") as f:
        data = f.read().split("\n")[:-1]
    return data

instructions = read_instructions("day14.txt")
#instructions = read_instructions("test.txt")

# PART 1
"""
MASK_LENGTH = 36
mask = ""
memory = {}
for inst in instructions:
    if inst.startswith("mask"):
        mask = inst[7:]
    else:
        pos = inst[4:inst.index("]")]
        num = int(inst[inst.index("=")+2:])
        bin_num = list(bin(num)[2:])
        bin_num = ["0"]*(MASK_LENGTH-len(bin_num)) + bin_num
        for i in range(MASK_LENGTH):
            if mask[i] == "1":
                bin_num[i] = "1"
            elif mask[i] == "0":
                bin_num[i] = "0"
        bin_num = "".join(bin_num)
        memory[pos] = int(bin_num, 2)
print(sum(memory.values()))
"""

# PART 2

def get_addr(pos):
    n_x = pos.count("X")
    n_addr = 2**n_x
    addresses = [[] for _ in range(n_addr)]
    consecutive = 2**(n_x-1)
    for bit in pos:
        if bit != "X":
            for i in range(n_addr):
                addresses[i].append(bit)
        else:
            wrote = 0
            write_zeros = True
            for i in range(n_addr):
                if wrote == consecutive:
                    wrote = 0
                    write_zeros = not write_zeros
                if write_zeros:
                    addresses[i].append("0")
                else:
                    addresses[i].append("1")
                wrote += 1
            consecutive /= 2
    return addresses


MASK_LENGTH = 36
mask = ""
memory = {}

for inst in instructions:
    if inst.startswith("mask"):
        mask = inst[7:]
    else:
        pos = int(inst[4:inst.index("]")])
        bin_pos = list(bin(pos)[2:])
        bin_pos = ["0"]*(MASK_LENGTH-len(bin_pos)) + bin_pos
        num = int(inst[inst.index("=")+2:])
        for i in range(MASK_LENGTH):
            if mask[i] == "X":
                bin_pos[i] = "X"
            else:
                bin_pos[i] = str(int(bin_pos[i]) | int(mask[i]))
        bin_pos = "".join(bin_pos)
        addresses = get_addr(bin_pos)
        for address in addresses:
            address = "".join(address)
            memory[address] = num

print(sum(memory.values()))
