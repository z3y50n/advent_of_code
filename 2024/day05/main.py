def read_data(filename):
    with open(filename, 'r') as f:
        rules, updates = f.read().strip().split('\n\n')

    return rules.split('\n'), [u.split(',') for u in updates.split('\n')]


def get_rules_map(rules: list[str]) -> dict[str, list[list[str]]]:
    rules_map = {}
    for rule in rules:
        a, b = rule.split('|')
        if a in rules_map:
            rules_map[a].append(b)
        else:
            rules_map[a] = [b]
    return rules_map


def part1(rules: list[str], updates: list[list[str]]) -> int:
    rules_map = get_rules_map(rules)
    ret = 0
    bad_idx = []
    for u_idx, update in enumerate(updates):
        right = True
        for i in range(len(update) - 1):
            for j in range(i+1, len(update)):
                if update[j] in rules_map and update[i] in rules_map[update[j]]:
                    right = False
                    bad_idx.append(u_idx)
                    break
        if right:
            ret += int(update[len(update) // 2])
    return ret,bad_idx


def part2(rules: list[str], updates: list[list[str]], bad: list[int]):
    rules_map = get_rules_map(rules)
    ret = 0
    for u_idx, update in enumerate(updates):
        if u_idx not in bad:
            continue
        n = len(update)
        for i in range(n):
            swapped = False
            for j in range(n - i - 1):
                if update[j+1] in rules_map and update[j] in rules_map[update[j+1]]:
                    update[j], update[j+1] = update[j+1], update[j]
                    swapped = True
            if not swapped:
                break
        ret += int(update[n // 2])
    return ret


if __name__ == "__main__":
    t_rules, t_updates = read_data('test_input')
    rules, updates = read_data('input')

    t_res, t_bad = part1(t_rules, t_updates)
    res, bad = part1(rules, updates)
    assert t_res == 143
    print(res)

    assert part2(t_rules, t_updates, t_bad) == 123
    print(part2(rules, updates, bad))
    
