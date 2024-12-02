from sys import stdin


def parse_report(line):
    return list(map(int, line.split()))


def is_safe_report(report):
    deltas = [b - a for a, b in zip(report, report[1:])]
    return all(-3 <= d <= -1 for d in deltas) or all(1 <= d <= 3 for d in deltas)


def is_safe_report_with_damping(report):
    damped_reports = [report[:i] + report[i + 1 :] for i in range(len(report))]
    return is_safe_report(report) or any(map(is_safe_report, damped_reports))


def main():
    reports = list(map(parse_report, stdin))
    print(sum(map(is_safe_report, reports)))
    print(sum(map(is_safe_report_with_damping, reports)))


if __name__ == "__main__":
    main()
