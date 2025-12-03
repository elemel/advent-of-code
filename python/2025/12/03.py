import sys


def get_joltages(line):
    for i in range(len(line) - 1):
        for j in range(i + 1, len(line)):
            yield int(line[i] + line[j])


def get_max_joltage(line, length):
    if length == 1:
        return max(line)

    prefix = line[: 1 - length]
    max_digit = max(prefix)
    min_index = min(i for i, digit in enumerate(prefix) if digit == max_digit)
    suffix = line[min_index + 1 :]
    return max_digit + get_max_joltage(suffix, length - 1)


def solve_part_1(lines):
    return sum(max(get_joltages(line)) for line in lines)


def solve_part_2(lines):
    return sum(int(get_max_joltage(line, 12)) for line in lines)


def main():
    lines = [line.strip() for line in sys.stdin]
    print(solve_part_1(lines))
    print(solve_part_2(lines))


if __name__ == "__main__":
    main()
