import sys
from heapq import heappush, heappop
from math import prod


def distance_squared(a, b):
    ax, ay, az = a
    bx, by, bz = b

    return (bx - ax) ** 2 + (by - ay) ** 2 + (bz - az) ** 2


def parse_position(line):
    return tuple(int(s) for s in line.split(","))


def solve_part_1(lines):
    positions = [parse_position(line) for line in lines]
    q = []

    for i, a in enumerate(positions[:-1]):
        for b in positions[i + 1 :]:
            d = distance_squared(a, b)
            heappush(q, (d, a, b))

    circuits_dict = {p: {p} for p in positions}

    for _ in range(1000):
        d, a, b = heappop(q)

        if circuits_dict[a] is not circuits_dict[b]:
            for c in circuits_dict.pop(b):
                circuits_dict[a].add(c)
                circuits_dict[c] = circuits_dict[a]

    circuits = sorted(set(frozenset(v) for v in circuits_dict.values()), key=len)
    return prod(len(c) for c in circuits[-3:])


def solve_part_2(lines):
    positions = [parse_position(line) for line in lines]
    q = []

    for i, a in enumerate(positions[:-1]):
        for b in positions[i + 1 :]:
            d = distance_squared(a, b)
            heappush(q, (d, a, b))

    circuits_dict = {p: {p} for p in positions}
    circuits_by_id = {id(c): c for c in circuits_dict.values()}

    while True:
        d, a, b = heappop(q)

        if circuits_dict[a] is not circuits_dict[b]:
            other = circuits_dict.pop(b)

            for c in other:
                circuits_dict[a].add(c)
                circuits_dict[c] = circuits_dict[a]

            circuits_by_id.pop(id(other))

            if len(circuits_by_id) == 1:
                ax, ay, az = a
                bx, by, bz = b

                return ax * bx


def main():
    lines = list(sys.stdin)
    print(solve_part_1(lines))
    print(solve_part_2(lines))


if __name__ == "__main__":
    main()
