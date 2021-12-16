from math import prod


def read_input(filename):
    with open(filename, "r") as f:
        data = f.read().strip()
    return data


def hex_to_bin(data):
    message = []
    for c in data:
        bit = bin(int(c, 16))[2:]
        bit = bit.zfill(4)
        message.append(bit)
    return "".join(message)


def bin_to_int(message):
    return int(message, 2)


SYMBOLS = {
    0: sum,
    1: prod,
    2: min,
    3: max,
    5: lambda x, y: x > y,
    6: lambda x, y: x < y,
    7: lambda x, y: x == y,
}

message = hex_to_bin(read_input("input.txt"))
test1 = hex_to_bin("D2FE28")
test2 = hex_to_bin("8A004A801A8002F478")
test3 = hex_to_bin("620080001611562C8802118E34")
test4 = hex_to_bin("C0015000016115A2E0802F182340")
test5 = hex_to_bin("A0016C880162017C3686B18A3D4780")


def parse(message, t):
    if t == 4:
        s, v = parse_value(message)
    else:
        s, v = parse_operator(message, t)
    return s, v


def parse_operator(message, t):
    global s_v
    l_t = message[0]
    values = []  # operator's values
    if l_t == "0":
        total_bits = bin_to_int(message[1:16])
        o_s = 16  # operator size
        init = 16
        while o_s < init + total_bits:
            s_v += bin_to_int(message[o_s : o_s + 3])
            p_t = bin_to_int(message[o_s + 3 : o_s + 6])
            o_s += 6
            s, v = parse(message[o_s:], p_t)
            values.append(v)
            o_s += s
    else:
        num_package = bin_to_int(message[1:12])
        o_s = 12  # operator_size
        for i in range(num_package):
            s_v += bin_to_int(message[o_s : o_s + 3])
            p_t = bin_to_int(message[o_s + 3 : o_s + 6])
            o_s += 6
            s, v = parse(message[o_s:], p_t)
            values.append(v)
            o_s += s

    v = calculate(t, values)
    return o_s, v


def parse_value(message):
    s = 0
    val = []
    while True:
        num = message[s : s + 5]
        s += 5
        val.append(num[1:])
        if num[0] == "0":
            break
    val = bin_to_int("".join(val))
    return s, val


def calculate(t, values):
    if t < 4:
        if len(values) == 1:
            return values[0]
        return SYMBOLS[t](values)
    else:
        assert len(values) == 2
        res = SYMBOLS[t](*values)
        if res == True:
            return 1
        return 0


def solve(message):
    global s_v
    v = bin_to_int(message[0:3])
    t = bin_to_int(message[3:6])
    s_v += v
    size, res = parse(message[6:], t)
    return size, res


# PART 1
def part1(message):
    global s_v
    s_v = 0
    solve(message)
    return s_v


assert part1(test1) == 6
assert part1(test2) == 16
assert part1(test3) == 12
assert part1(test4) == 23
assert part1(test5) == 31
print(part1(message))


# PART 2
def part2(message):
    global s_v
    s_v = 0
    s, res = solve(message)
    return res


# Could have added some assert statements here as well
print(part2(message))
