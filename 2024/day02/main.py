def read_data(filename):
    with open(filename, "r") as f:
        data = f.read().strip().split("\n")
    return [list(map(int, row.split())) for row in data]


def is_safe(report: list[int]) -> bool:
    diffs = [report[i] - report[i - 1] for i in range(1, len(report))]
    return (
        all([diff > 0 for diff in diffs]) or all([diff < 0 for diff in diffs])
    ) and all([0 < abs(diff) < 4 for diff in diffs])


def part1(reports: list[list[int]]) -> int:
    return sum(is_safe(report) for report in reports)


def part2(reports: list[list[int]]) -> int:
    return sum(
        any(is_safe(report[:j] + report[j + 1 :]) for j in range(len(report)))
        for report in reports
    )


if __name__ == "__main__":
    reports = read_data("input")
    test_reports = read_data("test_input")
    assert (part1(test_reports)) == 2
    print(part1(reports))
    assert part2(test_reports) == 4
    print(part2(reports))
