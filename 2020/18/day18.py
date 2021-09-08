import math

def read_data(filename):
    with open(filename, "r") as f:
        data = f.read().split("\n")[:-1]
    ret = []
    for exp in data:
        e = []
        for c in exp:
            if c == " ":
                continue
            elif c=="+" or c == "*" or c=="(" or c==")":
                e.append(c)
            else:
                e.append(int(c))
        ret.append(e)
    return ret

data = read_data("day18.txt")

def evaluate(expression, part):
    numbers = []
    operators = []
    temp_numbers = []
    temp_operators = []
    if part == "part 1":
        operation = operation1
    else:
        operation = operation2
    for c in expression:
        if isinstance(c, int):
            numbers.append(c)
        elif c == ")":
            temp_numbers.append(numbers.pop())
            while operators[-1] != "(":
                temp_numbers.append(numbers.pop())
                temp_operators.append(operators.pop())
            operators.pop() # Remove the opening (
            numbers.append(operation(temp_numbers[::-1], temp_operators[::-1]))
            temp_numbers = []
            temp_operators = []
        else:
            operators.append(c)
    return operation(numbers, operators)

def execute(expressions, part):
    total = 0
    for exp in expressions:
        total += evaluate(exp, part)
    return total


# PART 1
def operation1(numbers, operators):
    total = numbers[0]
    for i in range(1, len(numbers)):
        if operators[i-1] == "+":
            total += numbers[i]
        else:
            total *= numbers[i]
    return total

# PART 2
def operation2(numbers, operators):
    total = [numbers[0]]
    for i in range(1, len(numbers)):
        if operators[i-1] == "+":
            total[-1] += numbers[i]
        else:
            total.append(numbers[i])
    return math.prod(total)
    
print(execute(data, "part 1"))
print(execute(data, "part 2"))
