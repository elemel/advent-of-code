from sys import stdin

DIRECTION_DICT = dict(D=(0, 1), L=(-1, 0), R=(1, 0), U=(0, -1))
DIRECTION_LIST = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def print_grid(grid):
    min_x = min(x for x, y in grid)
    min_y = min(y for x, y in grid)

    max_x = max(x for x, y in grid)
    max_y = max(y for x, y in grid)

    for y in range(min_y, max_y + 1):
        print("".join(".#"[(x, y) in grid] for x in range(min_x, max_x + 1)))


def add(a, b):
    ax, ay = a
    bx, by = b

    return ax + bx, ay + by


def det(a, b):
    ax, ay = a
    bx, by = b

    return ax * by - bx * ay


def mul(a, b):
    if type(a) is tuple and type(b) is int:
        ax, ay = a
        return ax * b, ay * b
    elif type(a) is int and type(b) is tuple:
        bx, by = b
        return a * bx, a * by
    else:
        assert False


def fill(grid, p, v):
    s = [p]

    while s:
        p = s.pop()

        if p in grid:
            continue

        grid[p] = v

        for d in DIRECTION_DICT.values():
            np = add(p, d)

            if np in grid:
                continue

            s.append(np)


def parse_instruction_for_part_1(line):
    d, n, _ = line.split()

    d = DIRECTION_DICT[d]
    n = int(n)

    return d, n


def parse_instruction_for_part_2(line):
    _, _, c = line.split()
    c = c[2:][:-1]

    n = int(c[:-1], 16)
    d = DIRECTION_LIST[int(c[-1])]

    return d, n


def solve_part_1(instrs):
    grid = {}

    p = 0, 0
    grid[p] = "#ffffff"

    for d, n in instrs:
        for _ in range(n):
            p = add(p, d)
            grid[p] = "#ffffff"

    fill(grid, (1, 1), "#ff0000")
    return len(grid)


def solve_part_2(instructions):
    p = 0, 0
    d = 1, 0
    a = 0

    for nd, n in instructions:
        turn = det(d, nd)

        if turn == -1:
            n -= 1
        elif turn == 1:
            a += det(p, add(p, d))
            p = add(p, d)

        np = add(p, mul(nd, n))
        a += det(p, np)

        p = np
        d = nd

    return a // 2


def main():
    lines = [*stdin]
    instructions_1 = [*map(parse_instruction_for_part_1, lines)]
    instructions_2 = [*map(parse_instruction_for_part_2, lines)]

    print(solve_part_1(instructions_1))
    print(solve_part_2(instructions_2))


if __name__ == "__main__":
    main()
