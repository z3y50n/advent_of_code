def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read().strip()
    return data

message = read_data('input.txt')

t1 = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
t2 = 'bvwbjplbgvbhsrlpgdmjqwftvncz'
t3 = 'nppdvjthqldpwncqszvftbrmjlhg'
t4 = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'
t5 = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'

def find_start(message, length):
    for i in range(len(message) - length):
        seq = message[i:i+length]
        if len(set(seq)) == length:
            return i+length

# PART 1
assert find_start(t1, 4) == 7
assert find_start(t2, 4) == 5
assert find_start(t3, 4) == 6
assert find_start(t4, 4) == 10
assert find_start(t5, 4) == 11
print(find_start(message, 4))

# PART 2
assert find_start(t1, 14) == 19
assert find_start(t2, 14) == 23
assert find_start(t3, 14) == 23
assert find_start(t4, 14) == 29
assert find_start(t5, 14) == 26
print(find_start(message, 14))