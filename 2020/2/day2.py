with open('day2.txt', 'r') as fp:
    data = fp.read().split('\n')

data = [row.split(" ") for row in data]
ranges = [row[0].split("-") for row in data]
ranges = [list(map(lambda x: int(x), row)) for row in ranges]
print(data)
valid = 0
for i in range(len(data)):
    count = 0
    pos_1 = ranges[i][0]-1
    pos_2 = ranges[i][1]-1
    letter = data[i][1][0]
    password = data[i][2]
    if pos_2 < len(password) and ((letter == password[pos_1]) != (letter == password[pos_2])):
        valid+=1

print(valid)
