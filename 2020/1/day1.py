with open('day1.txt', 'r') as fp:
    data = fp.read().split("\n")

data = list(map(lambda x: int(x), data))

# PART 1
for i in range(len(data)):
    for j in range(i, len(data)):
        if data[i]+data[j] == 2020:
            print(data[i]*data[j])

# PART 2
for i in range(len(data)):
    for j in range(i, len(data)):
        for k in range(j, len(data)):
            if data[i]+data[j]+data[k] == 2020:
                print(data[i]*data[j]*data[k])
