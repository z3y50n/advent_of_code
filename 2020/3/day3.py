with open('day3.txt', 'r') as f:
    data = f.read().split("\n")[:-1]

#Part 1
pos = 0
trees = 0
for i in range(len(data)-1):
    pos += 3
    if data[i+1][pos%len(data[i])] == "#":
        trees += 1
print(trees)

#Part 2
def traverse(right, down):
    pos = 0
    trees = 0
    for i in range(0, len(data)-1, down):
        pos += right
        if data[i+down][pos%len(data[i])] == "#":
            trees += 1
    return trees

mul = 1
slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
for slope in slopes:
    mul *= traverse(*slope)

print(mul)


