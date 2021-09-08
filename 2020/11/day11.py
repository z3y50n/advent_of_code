def get_seats(filename):
    with open(filename, "r") as f:
        data = f.read().split("\n")[:-1]
    for i in range(len(data)):
        data[i] = list(data[i])
    return data

seats = get_seats("day11.txt")

def print_seats(seats):
    for i in range(len(seats)):
        print('\t', end="")
        for j in range(len(seats[i])):
            print(seats[i][j], end=" ")
        print("\n")

# PART 1        
def calc_next(x,y, seats):
    status = "#"
    if seats[x][y] == "L":
        for i in range(x-1,x+2):
            if i < 0 or i >= len(seats): continue
            for j in range(y-1, y+2):
                if j < 0 or (i==x and j==y) or j >= len(seats[i]): continue
                if seats[i][j] == "#":
                    status = "L"
                    break
            if status == "L": break
    elif seats[x][y] == "#":
        cnt = 0
        for i in range(x-1,x+2):
            if i < 0 or i >= len(seats): continue
            for j in range(y-1, y+2):
                if j < 0 or (i==x and j==y) or j >= len(seats[i]): continue
                if seats[i][j] == "#": cnt += 1
        if cnt > 3: status = "L"
    else:
        status =  "."
    return status

"""
new = [x[:] for x in seats]
for round in range(100):
    for i in range(len(seats)):
        for j in range(len(seats[i])):
            new[i][j] = calc_next(i,j,seats)
    seats = [x[:] for x in new]
"""

# PART 2
def calc_next2(x, y, seats):
    status = "#"
    if seats[x][y] == "L":
        for i in range(-1,2):
            for j in range(-1,2):
                new_x = x + i
                new_y = y + j
                if new_x == x and new_y == y: continue
                while new_x>=0 and new_y>=0 and new_x<len(seats) and new_y<len(seats[0]):
                    if seats[new_x][new_y] == "#":
                        status = "L"
                        break
                    elif seats[new_x][new_y] == "L": break
                    new_x += i
                    new_y += j
                if status == "L": break
            if status == "L": break
    elif seats[x][y] == "#":
        cnt = 0
        for i in range(-1,2):
            for j in range(-1,2):
                new_x = x + i
                new_y = y + j
                if new_x == x and new_y == y: continue
                while new_x>=0 and new_y>=0 and new_x<len(seats) and new_y<len(seats[0]):
                    if seats[new_x][new_y] == "#":
                        cnt += 1
                        break
                    elif seats[new_x][new_y] == "L": break
                    new_x += i
                    new_y += j
        if cnt > 4: status = "L"        
    else:
        status =  "."
    return status

new = [x[:] for x in seats]
for round in range(85):
    for i in range(len(seats)):
        for j in range(len(seats[i])):
            new[i][j] = calc_next2(i,j,seats)
    seats = [x[:] for x in new]

cnt = 0
for i in seats:
    for j in i:
        if j == "#": cnt += 1
print(cnt)
