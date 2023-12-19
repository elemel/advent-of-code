from sys import stdin
from collections import deque

LEFT = -1, 0
RIGHT = 1, 0
UP = 0, -1
DOWN = 0, 1

DIRECTIONS = [LEFT, RIGHT, UP, DOWN]


def add(a, b):
    ax, ay = a
    bx, by = b

    return ax + bx, ay + by


def sub(a, b):
    ax, ay = a
    bx, by = b

    return ax - bx, ay - by


def solve(grid, position, direction):
    queue = deque()
    visited = set()

    queue.append((position, direction))

    while queue:
        state = queue.popleft()

        if state in visited:
            continue

        visited.add(state)
        position, direction = state

        tile = grid[position]
        new_directions = [direction]

        if tile == "/":
            if direction == RIGHT:
                new_directions = [UP]
            elif direction == LEFT:
                new_directions = [DOWN]
            elif direction == DOWN:
                new_directions = [LEFT]
            elif direction == UP:
                new_directions = [RIGHT]
            else:
                assert False
        elif tile == "\\":
            if direction == RIGHT:
                new_directions = [DOWN]
            elif direction == LEFT:
                new_directions = [UP]
            elif direction == DOWN:
                new_directions = [RIGHT]
            elif direction == UP:
                new_directions = [LEFT]
            else:
                assert False
        elif tile == "|":
            if direction in [LEFT, RIGHT]:
                new_directions = [UP, DOWN]
        elif tile == "-":
            if direction in [UP, DOWN]:
                new_directions = [LEFT, RIGHT]

        for new_direction in new_directions:
            new_position = add(position, new_direction)

            if new_position in grid:
                queue.append((new_position, new_direction))

    energized = {p for p, d in visited}
    return len(energized)


def main():
    grid = {(x, y): t for y, l in enumerate(stdin) for x, t in enumerate(l.strip())}
    print(solve(grid, (0, 0), RIGHT))

    min_x = min(x for x, y in grid)
    min_y = min(y for x, y in grid)
    max_x = max(x for x, y in grid)
    max_y = max(y for x, y in grid)

    edges = [(x, y) for x, y in grid if x in [min_x, max_x] or y in [min_y, max_y]]
    print(
        max(
            solve(grid, p, d)
            for p in edges
            for d in DIRECTIONS
            if sub(p, d) not in grid
        )
    )


if __name__ == "__main__":
    main()
