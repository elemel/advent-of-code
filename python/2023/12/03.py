import sys
from sys import stdin
from collections import deque
from math import prod


def get_neighbors(position):
    x, y = position

    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dx or dy:
                yield x + dx, y + dy


def is_symbol(char):
    return not char.isdigit() and char != "."


def is_part_number(grid, positions):
    neighbors = {n for p in positions for n in get_neighbors(p) if n not in positions}
    return any(is_symbol(grid.get(n, ".")) for n in neighbors)


def get_part_numbers(grid):
    for (x, y), char in grid.items():
        if char.isdigit() and not grid.get((x - 1, y), ".").isdigit():
            buffer = [char]
            positions = {(x, y)}

            for i in range(1, sys.maxsize):
                position = (x + i, y)
                char = grid.get(position, ".")

                if not char.isdigit():
                    break

                buffer.append(char)
                positions.add(position)

            if is_part_number(grid, positions):
                yield int("".join(buffer))


def get_part_number(grid, position):
    char = grid.get(position, ".")

    if not char.isdigit():
        return None

    x, y = position
    buffer = deque([char])

    for x2 in range(x - 1, x - 1000, -1):
        char = grid.get((x2, y), ".")

        if not char.isdigit():
            break

        buffer.appendleft(char)

    for x2 in range(x + 1, x + 1000):
        char = grid.get((x2, y), ".")

        if not char.isdigit():
            break

        buffer.append(char)

    return int("".join(buffer))


def get_gear_ratio(grid, position):
    part_numbers = {get_part_number(grid, n) for n in get_neighbors(position)} - {None}
    return prod(part_numbers) if len(part_numbers) == 2 else None


def get_gear_ratios(grid):
    for position, char in grid.items():
        if char == "*":
            gear_ratio = get_gear_ratio(grid, position)

            if gear_ratio is not None:
                yield gear_ratio


def main():
    grid = {(x, y): c for y, l in enumerate(stdin) for x, c in enumerate(l) if c != "."}

    print(sum(get_part_numbers(grid)))
    print(sum(get_gear_ratios(grid)))


if __name__ == "__main__":
    main()
