from sys import stdin


def parse_report(line):
    return [int(token) for token in line.split()]


def is_safe_report(report):
    deltas = [b - a for a, b in zip(report, report[1:])]
    return all(-3 <= d <= -1 for d in deltas) or all(1 <= d <= 3 for d in deltas)


def is_safe_report_with_tolerance(report):
    return is_safe_report(report) or any(
        is_safe_report(report[:i] + report[i + 1 :]) for i in range(len(report))
    )


def main():
    reports = [parse_report(line) for line in stdin]
    print(sum(is_safe_report(report) for report in reports))
    print(sum(is_safe_report_with_tolerance(report) for report in reports))


if __name__ == "__main__":
    main()
