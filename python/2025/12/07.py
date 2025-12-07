import sys
from functools import cache


def solve_part_1(lines):
    beams = set()
    count = 0

    for line in lines:
        for i, symbol in enumerate(line):
            if symbol == "S":
                beams.add(i)
            elif symbol == "^":
                if i in beams:
                    beams.remove(i)
                    beams.add(i - 1)
                    beams.add(i + 1)
                    count += 1

    return count


def solve_part_2(lines):
    @cache
    def solve(x, y):
        if y >= len(lines):
            return 1

        symbol = lines[y][x]

        if symbol == ".":
            return solve(x, y + 1)
        elif symbol == "^":
            return solve(x - 1, y + 1) + solve(x + 1, y + 1)
        else:
            raise Exception()

    x = lines[0].index("S")
    return solve(x, 1)


def main():
    lines = list(sys.stdin)
    print(solve_part_1(lines))
    print(solve_part_2(lines))


if __name__ == "__main__":
    main()
