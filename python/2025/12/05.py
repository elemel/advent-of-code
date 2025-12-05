import sys


# Step must be 1
def merge_ranges(ranges):
    sorted_ranges = sorted(ranges, key=(lambda r: r.start))
    result = []

    if not sorted_ranges:
        return result

    last = sorted_ranges[0]

    if last.step != 1:
        raise ValueError("Step must be 1")

    for current in sorted_ranges[1:]:
        if current.step != 1:
            raise ValueError("Step must be 1")

        if last.stop < current.start:
            # Disjoint
            result.append(last)
            last = current
        elif last.stop < current.stop:
            # Merge
            last = range(last.start, current.stop)

    result.append(last)
    return result


def parse_fresh_range(line):
    start_str, stop_str = line.split("-")

    start = int(start_str)
    stop = int(stop_str)  # Inclusive

    # In Python ranges, stop is excluded
    return range(start, stop + 1)


def parse_lines(lines):
    i = lines.index("")
    fresh_ranges = [parse_fresh_range(line) for line in lines[:i]]
    ingredients = [int(line) for line in lines[i + 1 :]]
    return fresh_ranges, ingredients


def solve_part_1(lines):
    fresh_ranges, ingredients = parse_lines(lines)
    return sum(any(i in r for r in fresh_ranges) for i in ingredients)


def solve_part_2(lines):
    fresh_ranges, _ = parse_lines(lines)
    return sum(len(r) for r in merge_ranges(fresh_ranges))


def main():
    lines = [line.strip() for line in sys.stdin]
    print(solve_part_1(lines))
    print(solve_part_2(lines))


if __name__ == "__main__":
    main()
