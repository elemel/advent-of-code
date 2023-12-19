from sys import stdin
from functools import cache


def parse_spring_line(line):
    a, b = line.split()
    return a, tuple(int(c) for c in b.split(","))


@cache
def count_matches(pattern, group_sizes):
    if not group_sizes:
        return int("#" not in pattern)

    pattern = pattern.replace(".", " ").strip()
    result = 0

    n = group_sizes[0]
    ms = group_sizes[1:]

    for i in range(len(pattern) - n + 1):
        if all(pattern[j] in "?#" for j in range(i, i + n)):
            if i + n == len(pattern):
                result += len(ms) == 0
            elif pattern[i + n] == "#":
                pass
            else:
                result += count_matches(pattern[i + n + 1 :], ms)

        if pattern[i] == "#":
            break

    return result


def main():
    spring_lines = [parse_spring_line(l) for l in stdin]

    total = 0

    for pattern, group_sizes in spring_lines:
        result = count_matches(pattern, group_sizes)
        total += result

    print(total)

    total = 0

    for pattern, group_sizes in spring_lines:
        result = count_matches("?".join([pattern] * 5), group_sizes * 5)
        total += result

    print(total)


if __name__ == "__main__":
    main()
