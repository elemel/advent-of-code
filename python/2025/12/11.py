import sys
from functools import cache


def parse_device(line):
    a, bs_str = line.split(": ")
    bs = bs_str.split()
    return a, bs


def solve_part_1(lines):
    devices = dict(parse_device(line) for line in lines)

    @cache
    def solve(a):
        if a == "out":
            return 1

        return sum(solve(b) for b in devices[a])

    return solve("you")


def solve_part_2(lines):
    devices = dict(parse_device(line) for line in lines)

    @cache
    def solve(a, dac, fft):
        if a == "out":
            return int(dac and fft)

        return sum(solve(b, dac or b == "dac", fft or b == "fft") for b in devices[a])

    return solve("svr", False, False)


def main():
    lines = list(sys.stdin)
    print(solve_part_1(lines))
    print(solve_part_2(lines))


if __name__ == "__main__":
    main()
