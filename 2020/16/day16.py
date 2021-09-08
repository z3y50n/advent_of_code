def read_data(filename):
    with open(filename, "r") as f:
        data = f.read().split("nearby tickets:\n")
    rules = data[0].split("\n")[:-1]
    tickets = data[1].split("\n")[:-1]

    rules = [rule.split(": ")[1].split(" or ") for rule in rules]
    rules = [list(map(lambda x: tuple(map(int,x.split("-"))), rule)) for rule in rules]
    tickets = [tuple(map(int, ticket.split(","))) for ticket in tickets]

    return rules, tickets

rules, tickets = read_data("day16.txt")

# PART 1
invalid = []
idx = []
valid_tickets = []
for ticket in tickets:
    for num in ticket:
        valid = False
        for rule in rules:
            if (num>=rule[0][0] and num<=rule[0][1]) or (num>=rule[1][0] and num<=rule[1][1]):
                valid = True
                break
        if not valid:
            idx.append(tickets.index(ticket))
            invalid.append(num)
            break

valid_tickets = [tickets[i] for i in range(len(tickets)) if i not in idx]
print(sum(invalid))

# PART 2
my_ticket = tuple(map(int,"151,71,67,113,127,163,131,59,137,103,73,139,107,101,97,149,157,53,109,61".split(",")))

rules_idx = [[] for _ in range(len(rules))]

for j, rule in enumerate(rules):
    for i in range(0, len(my_ticket)):
        valid = True
        for ticket in valid_tickets:
            num = ticket[i]
            if (num<rule[0][0] or num>rule[0][1]) and (num<rule[1][0] or num>rule[1][1]):
                valid = False
                break
        if not valid:
            continue
        else:
            rules_idx[j].append(i)

for rule in rules_idx:
    print(rule)

final_rules = [-1]*len(rules)
while -1 in final_rules:
    for i, rule in enumerate(rules_idx):
        if len(rule) == 1:
            col = rule[0]
            final_rules[i] = col
            for other in rules_idx:
                if col in other:
                    idx = other.index(col)
                    other.pop(idx)
            break
print(final_rules)
mul = 1
for i in range(6):
    mul *= my_ticket[final_rules[i]]

print(mul)





