import sys


def parse_range(line):
    a, b = line.split("-")
    return int(a), int(b)


def parse_lines(lines):
    i = lines.index("")

    ranges = [parse_range(line) for line in lines[:i]]
    ingreds = [int(line) for line in lines[i + 1 :]]
    return ranges, ingreds


def solve_part_1(lines):
    ranges, ingreds = parse_lines(lines)

    count = 0

    for ingred in ingreds:
        for a, b in ranges:
            if a <= ingred <= b:
                count += 1
                break

    return count


def solve_part_2(lines):
    ranges, _ = parse_lines(lines)
    sorted_ranges = sorted(ranges)

    count = 0
    last_b = -1

    for a, b in sorted_ranges:
        a = max(a, last_b + 1)
        b = max(b, last_b)

        count += b - a + 1
        last_b = b

    return count


def main():
    lines = [line.strip() for line in sys.stdin]
    print(solve_part_1(lines))
    print(solve_part_2(lines))


if __name__ == "__main__":
    main()
