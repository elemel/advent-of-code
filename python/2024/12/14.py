from sys import stdin
from pyule import Vector2, parse_ints
from collections import defaultdict
from math import prod


def parse_robot(line):
    x, y, dx, dy = parse_ints(line)
    return Vector2(x, y), Vector2(dx, dy)


def solve_part_1(size, robots, time):
    quadrant_counts = defaultdict(int)

    for position, velocity in robots:
        new_position = (position + velocity * time) % size
        quadrant = (new_position - size // 2).sign()

        if all(quadrant):
            quadrant_counts[quadrant] += 1

    return prod(quadrant_counts.values())


def print_robots(size, robots, time):
    grid = {}

    for position, velocity in robots:
        new_position = (position + velocity * time) % size
        grid[new_position] = "#"

    for y in range(size.y):
        row = [2 * grid.get(Vector2(x, y), ".") for x in range(size.x)]
        print("".join(row))


def solve_part_2(size, robots, max_time):
    _, time = min(
        (solve_part_1(size, robots, time), time) for time in range(max_time + 1)
    )
    return time


def main():
    sizes = {12: Vector2(11, 7), 500: Vector2(101, 103)}
    robots = list(map(parse_robot, stdin))

    size = sizes[len(robots)]
    print(solve_part_1(size, robots, 100))
    print(solve_part_2(size, robots, 10000))


if __name__ == "__main__":
    main()
