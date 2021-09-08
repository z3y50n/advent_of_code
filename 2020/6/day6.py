def read_data(filename):
    with open(filename, "r") as f:
        groups = []
        answers = []
        for line in f.readlines():
            if line != "\n":
                answers.append(line.replace("\n", ""))
            else:
                groups.append(answers)
                answers = []
        return groups

groups = read_data("day6.txt")

# PART 1
def count_anyone(groups):
    count = 0
    for group in groups:
        count += len(set("".join(group)))
    return count

counts = count_anyone(groups)
print(counts)

# PART 2
def count_everyone(groups):
    count = 0
    for group in groups:
        letters = list(group[0])
        if len(group) > 1:
            for letter in letters:
                common = True
                for answer in group[1:]:
                    if letter not in answer:
                        common = False
                        break
                if common:
                    count += 1
        else:
            count += len(letters)
    return count

counts2 = count_everyone(groups)
print(counts2)
