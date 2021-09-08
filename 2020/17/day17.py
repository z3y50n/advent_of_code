def read_data(filename):
    with open(filename, "r") as f:
        data = f.read().split("\n")[:-1]
    state = list(map(list, data))
    return state

state = read_data("input.txt")
#state = [[".","#","."],[".",".","#"],["#","#","#"]]
grid_3d = [state] # 3D Part 1
grid_4d = [[state]] # 4D Part 2

def print_grid(grid):
    #3D Part 1
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j])
        print("\n")

def format_grid_3d(grid):
    for i in range(len(grid)):
        N = len(grid[i])
        for j in range(N):
            grid[i][j].insert(0, '.')
            grid[i][j].append(".")
        grid[i].insert(0, ['.']*(N+2))
        grid[i].append(['.']*(N+2))
        
    grid.insert(0, [['.']*(N+2) for _ in range(N+2)])
    grid.append([['.']*(N+2) for _ in range(N+2)])

    return grid

def format_grid_4d(grid):
    for k in range(len(grid)):
        M = len(grid[k])
        for i in range(M):
            N = len(grid[k][i])
            for j in range(N):
                grid[k][i][j].insert(0, '.')
                grid[k][i][j].append(".")
            grid[k][i].insert(0, ['.']*(N+2))
            grid[k][i].append(['.']*(N+2))
        
        grid[k].insert(0, [['.']*(N+2) for _ in range(N+2)])
        grid[k].append([['.']*(N+2) for _ in range(N+2)])
    grid.insert(0, [[['.']*(N+2) for _ in range(N+2)] for _ in range(M+2)])
    grid.append([[['.']*(N+2) for _ in range(N+2)] for _ in range(M+2)])

    return grid

def calc_state_3d(x, y, z, grid):
    ac_n = 0
    if grid[z][y][x] == "#": active = True
    else: active = False

    for i in range(-1,2):
        if z+i < 0 or z+i >= len(grid): continue
        for j in range(-1, 2):
            if y+j < 0 or y+j >= len(grid[z+i]): continue
            for k in range(-1, 2):
                if x+k < 0 or x+k >= len(grid[z+i][y+j]): continue
                if i==0 and j==0 and k==0: continue
                if grid[z+i][y+j][x+k] == "#": ac_n += 1
    if active:
        if ac_n >= 2 and ac_n <= 3:
            return "#"
    else:
        if ac_n == 3:
            return "#"
    return "."

def calc_state_4d(x, y, z, w, grid):
    ac_n = 0
    if grid[w][z][y][x] == "#": active = True
    else: active = False

    for h in range(-1, 2):
        if w+h < 0 or w+h >= len(grid): continue
        for i in range(-1,2):
            if z+i < 0 or z+i >= len(grid[w+h]): continue
            for j in range(-1, 2):
                if y+j < 0 or y+j >= len(grid[w+h][z+i]): continue
                for k in range(-1, 2):
                    if x+k < 0 or x+k >= len(grid[w+h][z+i][y+j]): continue
                    if h ==0 and i==0 and j==0 and k==0: continue
                    if grid[w+h][z+i][y+j][x+k] == "#": ac_n += 1
    if active:
        if ac_n >= 2 and ac_n <= 3:
            return "#"
    else:
        if ac_n == 3:
            return "#"
    return "."

def copy_list_3d(a):
    new = []
    for i in range(len(a)):
        level = []
        for j in range(len(a[i])):
            row = []
            for k in range(len(a[i][j])):
                row.append(a[i][j][k])
            level.append(row)
        new.append(level)
    return new

def copy_list_4d(a):
    new = []
    for h in range(len(a)):
        hyper = []
        for i in range(len(a[h])):
            level = []
            for j in range(len(a[h][i])):
                row = []
                for k in range(len(a[h][i][j])):
                    row.append(a[h][i][j][k])
                level.append(row)
            hyper.append(level)
        new.append(hyper)
    return new


def part_1(grid):
    steps = 6
    grid = format_grid_3d(grid)
    new_grid = copy_list_3d(grid)
    """
    print("ORIGINAL")
    print_grid(new_grid)
    print("-----------")
    """
    for i in range(steps):
        #print(f"STEP {i+1}\n-----------")
        for z in range(len(grid)):
            for y in range(len(grid[z])):
                for x in range(len(grid[z][y])):
                    new_grid[z][y][x] = calc_state_3d(x,y,z,grid)
        new_grid = format_grid_3d(new_grid)
        grid = copy_list_3d(new_grid)
        #print_grid(grid)
    return grid

def part_2(grid):
    steps = 6
    grid = format_grid_4d(grid)
    new_grid = copy_list_4d(grid)
    """
    print("ORIGINAL")
    print_grid(new_grid)
    print("-----------")
    """
    for i in range(steps):
        #print(f"STEP {i+1}\n-----------")
        for w in range(len(grid)):
            for z in range(len(grid[w])):
                for y in range(len(grid[w][z])):
                    for x in range(len(grid[w][z][y])):
                        new_grid[w][z][y][x] = calc_state_4d(x,y,z,w,grid)
        new_grid = format_grid_4d(new_grid)
        grid = copy_list_4d(new_grid)
        #print_grid(grid)
    return grid

def count_active_3d(grid):
    res = 0
    for z in grid:
        for y in z:
            for x in y:
                if x == "#": res += 1
    return res

def count_active_4d(grid):
    res = 0
    for w in grid:
        for z in w:
            for y in z:
                for x in y:
                    if x == "#": res += 1
    return res

final = part_1(grid_3d)
print(count_active_3d(final))

final2 = part_2(grid_4d)
print(count_active_4d(final2))
