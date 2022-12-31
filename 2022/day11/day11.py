class Monkey:
    def __init__(self, index, items, op, test, targets):
        self.index = index
        self.items = items
        self.op = op
        self.test = test
        self.targets = targets
        self.inspected = 0

    def __str__(self):
        return f'Monkey: {self.index}\nItems: {self.items}\nOperation: {self.op}\nTest: divisible by {self.test}\nTargets: {self.targets}'

    def get_inspected(self):
        return self.inspected

    def inspect(self):
        throws = []
        self.inspected += len(self.items)
        while len(self.items):
            item = self.items.pop(0)
            old = item
            worry_level = eval(self.op)
            worry_level //= 3
            if worry_level % self.test == 0:
                throws.append((worry_level, self.targets[0]))
            else:
                throws.append((worry_level, self.targets[1]))
        return throws

    def push_item(self, item):
        self.items.append(item)



def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read().strip().split('\n\n')

    monkeys = []
    for i, monkey in enumerate(data):
        lines = monkey.split('\n')
        items = list(map(int, lines[1].split(':')[1].split(', ')))
        op = lines[2].split('= ')[1]
        test = int(lines[3].split('by ')[1])
        targets = (int(lines[4].split('monkey ')[1]),
                   int(lines[5].split('monkey ')[1]))
        monkeys.append(Monkey(i, items, op, test, targets))
    return monkeys


t_monkeys = read_data('test_input.txt')
monkeys = read_data('input.txt')

def part1(monkeys):
    rounds = 20

    for r in range(rounds):
        for monkey in monkeys:
            throws = monkey.inspect()
            for throws in throws:
                monkeys[throws[1]].push_item(throws[0])
    inspections = [monkey.get_inspected() for monkey in monkeys]

    s = sorted(inspections, reverse=True)
    return s[0] * s[1]

assert part1(t_monkeys) == 10605
print(part1(monkeys))

