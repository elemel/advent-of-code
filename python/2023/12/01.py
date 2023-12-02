import sys

DIGIT_NAMES = "one two three four five six seven eight nine".split()


def parse_digits(line):
    for i in range(len(line)):
        if line[i].isdigit():
            yield int(line[i])

        for j, name in enumerate(DIGIT_NAMES, start=1):
            if line[i:].startswith(name):
                yield j


def solve_part_1(lines):
    total = 0

    for line in lines:
        digits = [int(c) for c in line if c.isdigit()]
        total += 10 * digits[0] + digits[-1]

    return total


def solve_part_2(lines):
    total = 0

    for line in lines:
        digits = list(parse_digits(line))
        total += 10 * digits[0] + digits[-1]

    return total


def main():
    lines = list(sys.stdin)
    print(solve_part_1(lines))
    print(solve_part_2(lines))


if __name__ == "__main__":
    main()
