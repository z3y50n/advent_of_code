def read_data(filename):
    with open(filename, "r") as f:
        data = f.read().split("\n")[:-1]
    return data

data = read_data("day5.txt")

# PART 1
def find_row_col(code):
    rows = list(range(128))
    cols = list(range(8))
    for l in code[:7]:
        if l == "F":
            rows = rows[:len(rows)//2]
        else:
            rows = rows[len(rows)//2:]
    for l in code[7:]:
        if l == "L":
            cols = cols[:len(cols)//2]
        else:
            cols = cols[len(cols)//2:]
    return (rows[0], cols[0])

def find_seats(data):
    ids = []
    for code in data:
        seat = find_row_col(code)
        ids.append(seat[0]*8 + seat[1])
    return sorted(ids)

seats = find_seats(data)
print(seats[-1])


# PART 2
def find_seat(seats):
    for i in range(seats[1], seats[-1]):
        if i != seats[i - seats[0]]:
            return i

print(find_seat(seats))
