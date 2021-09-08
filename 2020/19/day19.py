def read_data(filename):
    with open(filename, "r") as f:
        data = f.read().split("\n")[:-1]
    rules = data[:data.index("")]
    rules = {rule[:rule.index(":")]: rule[rule.index(":")+2:] for rule in rules}
    for rule in rules:
        if "a" in rules[rule] or "b" in rules[rule]:
            rules[rule] = rules[rule][1]
        else:
            rules[rule] = tuple(rules[rule].split(" "))
            if "|" in rules[rule]:
                idx = rules[rule].index("|")
                rules[rule] = [rules[rule][:idx], rules[rule][idx+1:]]

    messages = data[data.index("")+1:]
    return rules, messages


rules, messages = read_data("day19.txt")
#rules, messages = read_data("test.txt")

# PART 1
M_IDX = 0
def part1(rules, messages):
    global M_IDX
    total = 0
    for message in messages:
        M_IDX = 0
        if check(rules["0"], message) and M_IDX == len(message):
            total += 1
    return total

def check(rule, message):
    global M_IDX
    if rule == "a" or rule == "b":
        if message[M_IDX] == rule:
            M_IDX += 1
            return True
        return False
    elif isinstance(rule, tuple):
        for sub in rule:
            if not check(rules[sub], message):
                return False
        return True
    else:
        temp = M_IDX
        if check(rule[0], message): return True
        M_IDX = temp
        if check(rule[1], message): return True
        return False

#print(part1(rules, messages))

# PART 2
# I didn't manage to complete this by myself, based it on
# https://github.com/mebeim/aoc/blob/master/2020/solutions/day19.py

rules, messages = read_data("day19b.txt")
#rules, messages = read_data("testb.txt")

def parse_input(filename):
    with open(filename, "r") as f:
        data = f.read().split("\n")[:-1]
    rules = {}
    for line in map(str.rstrip, data):
        if not line:
            break

        rule_id, options = line.split(": ")
        rule_id = int(rule_id)

        if '"' in options:
            rule = options[1:-1]
        else:
            rule = []
            for option in options.split("|"):
                rule.append(tuple(map(int, option.split())))
        rules[rule_id] = rule
    return rules

rules = parse_input("day19b.txt")

def match(rules, message, rule=0, index=0):
    if index == len(message):
        return []

    rule = rules[rule]
    if type(rule) == str:
        if message[index] == rule:
            return [index + 1]
        return []

    matches = []
    for option in rule:
        sub_matches = [index]
        for sub_rule in option:
            new_matches = []
            for idx in sub_matches:
                new_matches += match(rules, message, sub_rule, idx)
            sub_matches = new_matches
        matches += sub_matches

    return matches

def part2(rules, messages):
    total = 0
    for message in messages:
        if len(message) in match(rules, message):
            total += 1
    return total

print(part2(rules, messages))
