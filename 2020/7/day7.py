def read_data(filename):
    with open(filename, "r") as f:
        data = f.read().split("\n")[:-1]

    rules = {}
    for rule in data:
        rule = rule.split(" ")
        bag = " ".join(rule[:2])
        contain = [(int(rule[i-1]), f"{rule[i]} {rule[i+1]}") if rule[i-1] != "no" else (0, "no bags") for i in range(5, len(rule), 4)]
        rules[bag] = contain

    return rules

rules = read_data("day7.txt")

# PART 1
def find_bags(rules):
    found = 1
    bags = ["shiny gold"]
    total_bags = []
    while found != 0:
        new_bags = []
        found = 0
        for bag, rule in rules.items():
            for candidate in bags:
                names = [pair[1] for pair in rule]
                if candidate in names and bag not in total_bags:
                    total_bags.append(bag)
                    new_bags.append(bag)
                    found += 1
        bags = new_bags.copy()
    return len(total_bags)

print(find_bags(rules))

#PART 2
def find_contains(bag, rules):
    total = 0
    for pair in rules[bag]:
        if pair[1] == "no bags":
            return 0
        total += pair[0] + pair[0] * find_contains(pair[1], rules)
    return total


print(find_contains("shiny gold", rules))
