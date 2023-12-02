import sys

DIGIT_NAMES = "one two three four five six seven eight nine".split()


def parse_digits(line):
    for i in range(len(line)):
        if line[i].isdigit():
            yield line[i]

        for j, name in enumerate(DIGIT_NAMES):
            if line[i:].startswith(name):
                yield str(j + 1)


def main():
    lines = list(sys.stdin)
    total = 0

    for line in lines:
        digits = [c for c in line if c.isdigit()]
        total += int(digits[0] + digits[-1])

    print(total)
    total = 0

    for line in lines:
        digits = list(parse_digits(line))
        total += int(digits[0] + digits[-1])

    print(total)


if __name__ == "__main__":
    main()
