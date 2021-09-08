#spoken = [20, 9, 11, 0, 1, 2]
spoken = [0, 3, 6,]

# PART 1
for i in range(len(spoken)+1, 2021):
    print(i, end="\r")
    last = spoken[-1]
    if spoken.count(last) == 1:
        spoken.append(0)
    else:
        indices = [j for j, x in enumerate(spoken) if x == last]
        diff = len(spoken)-1 - indices[-2]
        spoken.append(diff)
    
print(spoken[-1])

# PART 2
# Essentialy an improvement on part1 using memory
spoken = [20, 9, 11, 0, 1, 2]
#spoken = [0, 3, 6]
memory = {num:[i, -1] for i,num in enumerate(spoken)}
N = 30000000
#N = 2020

last = spoken[-1]
for i in range(len(spoken), N):
    print(i, end="\r")
    mem = memory[last]
    if mem[1] == -1:
        memory[0] = [i, memory[0][0]]
        last = 0
    else:
        last = mem[0] - mem[1]
        new = memory.get(last,[-1])
        memory[last] = [i, new[0]]

print("\n")
print(last)
