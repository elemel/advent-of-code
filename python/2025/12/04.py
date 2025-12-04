import sys

NEIGHBOR_OFFSETS = [(dx, dy) for dy in [-1, 0, 1] for dx in [-1, 0, 1] if dx or dy]


def vec_add(a, b):
    ax, ay = a
    bx, by = b
    return ax + bx, ay + by


def parse_grid(lines):
    grid = {}

    for y, line in enumerate(lines):
        for x, value in enumerate(line):
            grid[x, y] = value

    return grid


def get_neighbors(grid, position):
    for offset in NEIGHBOR_OFFSETS:
        neighbor_position = vec_add(position, offset)

        if neighbor_position in grid:
            yield grid[neighbor_position]


def can_remove(grid, position):
    return grid[position] == "@" and (
        sum(neighbor == "@" for neighbor in get_neighbors(grid, position)) < 4
    )


def solve_part_1(lines):
    grid = parse_grid(lines)
    return sum(can_remove(grid, position) for position in grid)


def solve_part_2(lines):
    grid = parse_grid(lines)
    progress = True
    result = 0

    while progress:
        progress = False

        for position in grid:
            if can_remove(grid, position):
                grid[position] = "."
                result += 1
                progress = True

    return result


def main():
    lines = [line.strip() for line in sys.stdin]
    print(solve_part_1(lines))
    print(solve_part_2(lines))


if __name__ == "__main__":
    main()
