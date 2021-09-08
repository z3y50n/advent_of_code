def read_data(filename):
    with open(filename, "r") as f:
        data = f.read().split("\n")[:-1]
    data[0] = int(data[0])
    data[1] = [int(num) if num != "x" else num for num in data[1].split(",")]
    return data

data = read_data("day13.txt")
# PART 1
def part_1(data):
    res = {}
    for i in range(len(data[1])):
        if data[1][i] != 'x':
            bid = data[1][i]
            while data[1][i] < data[0]:
                data[1][i] += bid
            res[bid] = data[1][i] - data[0]
    rid = min(res, key=res.get)
    return rid*res[rid]

#print(part_1(data))

# PART 2
# Solution uses Chinese Remainder Theorem
idxs = [i for i in range(len(data[1])) if data[1][i] != "x"]
numbers = [int(num) for num in data[1] if num != "x"]
print(numbers)
print(idxs)

def prod(arr):
    res = 1
    for n in arr:
        res *= n
    return res

N = prod(numbers)
y = []
for i in range(len(numbers)):
    y.append(N//numbers[i])

def extended_euclidean(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1-q*x0, x0
    if x1<0: x1 += b0
    return x1

z = []
for i in range(len(numbers)):
    z.append(extended_euclidean(int(y[i]), numbers[i]))

res = 0
for i in range(len(numbers)):
    res += (numbers[i]-idxs[i])*y[i]*z[i]

print(int(res%N))

"""
# My brute force solution, works for reasonable numbers
diffs = [0]
cnt = 0
data[1] = [17, "x", 13, 19]
#data[1] = [67, "x",7,59,61]
for i in range(1, len(data[1])):
    if data[1][i] == "x":
        cnt += 1
    else:
        diffs.append(cnt+1)
        cnt = 0
diffs = [sum(diffs[:i+1]) for i in range(len(diffs))]
print(diffs)
numbers = [int(num) for num in data[1] if num != "x"]
print(numbers)
time = 100000000000000
found = False

while not found:
    found = True
    time += numbers[0]
    for i in range(1, len(numbers)):
        div = (time+diffs[i]) / numbers[i]
        if div != int(div):
            found = False
            break
print(time)
"""
