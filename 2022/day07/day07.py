from collections import defaultdict

def read_data(filename):
    with open(filename, 'r') as f:
        return f.read().strip().split('\n')

data = read_data('input.txt')
t_data = read_data('test_input.txt')

def getFileTree(data):
    filetree = defaultdict(list)
    filetree['/'] = []
    currentDir = '/'
    for c in data[1:]:
        if c.startswith('$'):
            if c[2:4] == 'cd':
                dirName = c[5:].strip()
                if dirName != '..':
                    currentDir+= dirName + '/'
                else:
                    currentDir = '/'.join(currentDir.split('/')[:-2]) + '/'
        else:
            filetree[currentDir].append(c)
    return filetree

def calculateSize(filetree, path, filesizes):
    if path in filesizes:
        return filesizes[path]
    size = 0
    for p in filetree[path]:
        if p.startswith('dir'):
            size += calculateSize(filetree, path + p.split()[1] + '/', filesizes)
        else:
            size += int(p.split()[0])
    filesizes[path] = size
    return size

def part1(data):
    filetree = getFileTree(data)
    filesizes = {}
    calculateSize(filetree, '/', filesizes)
    t = 0
    for d in filesizes:
        if filesizes[d] <= 100000:
            t += filesizes[d]
    return t

assert part1(t_data) == 95437
print(part1(data))

def part2(data):
    filetree = getFileTree(data)
    filesizes = {}
    calculateSize(filetree, '/', filesizes)
    needed = 30000000 - 70000000 + filesizes['/'] 
    m = float('inf')
    for size in filesizes.values():
        if size >= needed and size < m:
            m = size
    return m

assert part2(t_data) == 24933642
print(part2(data))







