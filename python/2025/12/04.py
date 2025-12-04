import sys


def get_neighbor_positions(position):
    x, y = position
    return [(x + dx, y + dy) for dy in [-1, 0, 1] for dx in [-1, 0, 1] if dx or dy]


def can_access(grid, position):
    return sum(grid.get(neighbor_position) == "@" for neighbor_position in get_neighbor_positions(position)) < 4


def solve_part_1(lines):
    grid = {}

    for y, line in enumerate(lines):
        for x, value in enumerate(line):
            grid[x, y] = value

    return sum(grid[position] == "@" and can_access(grid, position) for position in grid)


def solve_part_2(lines):
    grid = {}

    for y, line in enumerate(lines):
        for x, value in enumerate(line):
            grid[x, y] = value

    progress = True
    result = 0

    while progress:
        progress = False

        for position in grid:
            if grid[position] == "@" and can_access(grid, position):
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
