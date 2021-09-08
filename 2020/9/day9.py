def read_data(filename):
    with open(filename, "r") as f:
        data = f.read().split("\n")[:-1]

    numbers = [int(number) for number in data]
    return numbers

numbers = read_data("day9.txt")

# PART 1
def part_1(numbers):
    for i in range(25, len(numbers)):
        check = False
        for j in range(i-25, i):
            for k in range(j, i):
                if numbers[i] == numbers[j] + numbers[k]:
                    check = True
                    break
            if check:
                break
        if not check:
            return numbers[i]

res = part_1(numbers)
print(res)

# PART 2
def part_2(numbers, res):
    limit = numbers.index(res)
    for i in range(limit):
        for j in range(i+1, limit):
            summ = sum(numbers[i:j])
            if summ == res:
                return min(numbers[i:j]) + max(numbers[i:j])


print(part_2(numbers, res))

