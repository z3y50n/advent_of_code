def read_data(filename):
    with open(filename, "r") as f:
        data = f.read().strip().split("\n")
    return [list(map(int, row.split())) for row in data]


def part1(reports: list[list[int]]) -> int:
    safes = 0
    for report in reports:
        diffs = []
        for i in range(1, len(report)):
            diffs.append(report[i] - report[i - 1])
        if (
            all([diff > 0 for diff in diffs]) or all([diff < 0 for diff in diffs])
        ) and all([0 < abs(diff) < 4 for diff in diffs]):
            safes += 1

    return safes


if __name__ == "__main__":
    reports = read_data("input")
    test_reports = read_data("test_input")
    assert (part1(test_reports)) == 2
    print(part1(reports))
