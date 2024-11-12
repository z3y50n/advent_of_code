from math import lcm

type Nodes = dict[str, tuple[str, str]]


def read_data(filename: str):
    with open(filename, "r") as f:
        data = f.read().strip().split("\n\n")
    instructions = data[0]
    rows = data[1].split("\n")
    nodes: Nodes = {}
    for row in rows:
        nodes[row[:3]] = (row[7:10], row[12:15])
    return instructions, nodes


def part1(instructions: str, nodes: Nodes):
    ways = 0
    instruction_idx = 0
    current_node = "AAA"
    while True:
        ways += 1
        choose_idx = 0
        if instructions[instruction_idx % len(instructions)] == "R":
            choose_idx = 1
        current_node = nodes[current_node][choose_idx]
        if current_node == "ZZZ":
            return ways
        instruction_idx += 1


def part2(instructions: str, nodes: Nodes):
    start_nodes = filter(lambda node: node.endswith("A"), nodes)
    cycles = []
    for start_node in start_nodes:
        node = start_node
        instruction_idx = 0
        steps = 0
        while True:
            steps += 1
            choose_idx = 0
            if instructions[instruction_idx % len(instructions)] == "R":
                choose_idx = 1
            node = nodes[node][choose_idx]
            instruction_idx += 1
            if node.endswith("Z"):
                cycles.append(steps)
                break

    return lcm(*cycles)


if __name__ == "__main__":
    test_instructions, test_nodes = read_data("test_input")
    instructions, nodes = read_data("input")
    assert part1(test_instructions, test_nodes) == 2
    print(part1(instructions, nodes))

    test_instructions, test_nodes = read_data("test_input2")
    assert part2(test_instructions, test_nodes) == 6
    print(part2(instructions, nodes))
