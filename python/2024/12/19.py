from sys import stdin
from functools import cache


def main():
    patterns_str, designs_str = stdin.read().split("\n\n")

    patterns = patterns_str.split(", ")
    designs = designs_str.split()

    @cache
    def solve(design):
        if not design:
            return 1

        return sum(
            solve(design[len(pattern) :])
            for pattern in patterns
            if design.startswith(pattern)
        )

    print(len(list(filter(solve, designs))))
    print(sum(map(solve, designs)))


if __name__ == "__main__":
    main()
