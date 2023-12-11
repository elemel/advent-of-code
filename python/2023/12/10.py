from sys import stdin

NORTH = 0, -1
SOUTH = 0, 1
WEST = -1, 0
EAST = 1, 0

PIPES = {
    "|": {NORTH, SOUTH},
    "-": {EAST, WEST},
    "L": {NORTH, EAST},
    "J": {NORTH, WEST},
    "7": {SOUTH, WEST},
    "F": {SOUTH, EAST},
}


def add(a, b):
    ax, ay = a
    bx, by = b

    return ax + bx, ay + by


def neg(a):
    ax, ay = a
    return -ax, -ay


def deduce_pipe(grid, position):
    directions = set()

    for direction in [NORTH, SOUTH, WEST, EAST]:
        new_position = add(position, direction)

        if new_position not in grid:
            continue

        new_pipe = grid[new_position]

        if new_pipe not in PIPES:
            continue

        if neg(direction) in PIPES[new_pipe]:
            directions.add(direction)

    pipes = [p for p in PIPES if PIPES[p] == directions]
    return pipes[0] if len(pipes) == 1 else None


def find_path(grid, start):
    position = start
    direction = min(PIPES[grid[start]])

    path = []

    while not path or position != start:
        position = add(position, direction)
        [direction] = [d for d in PIPES[grid[position]] if d != neg(direction)]
        path.append(position)

    return path


def is_inside(grid, path_set, position):
    if position in path_set:
        return False

    crossing_count = 0

    while position in grid:
        if position in path_set and grid[position] not in "7L":
            crossing_count += 1

        position = add(position, (1, 1))

    return crossing_count % 2 == 1


def main():
    grid = {(x, y): c for y, l in enumerate(stdin) for x, c in enumerate(l.strip())}

    [start] = [p for p, c in grid.items() if c == "S"]
    grid[start] = deduce_pipe(grid, start)

    path = find_path(grid, start)
    print(len(path) // 2)

    path_set = set(path)
    print(sum(is_inside(grid, path_set, p) for p in grid))


if __name__ == "__main__":
    main()
