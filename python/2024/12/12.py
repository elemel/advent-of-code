from sys import stdin
from itertools import count
from pyule import Vector2, parse_grid


def get_neighbors(position):
    for direction in Vector2.ORTHOGONAL_DIRECTIONS:
        yield position + direction


def pop_region(grid):
    position = next(iter(grid))
    char = grid[position]
    region = set()
    queue = {position}

    while queue:
        position = queue.pop()

        if grid.get(position) != char:
            continue

        grid.pop(position)
        region.add(position)

        for neighbor in get_neighbors(position):
            queue.add(neighbor)

    return region


def get_regions(grid):
    grid = dict(grid)

    while grid:
        yield pop_region(grid)


def get_edges(region):
    for position in region:
        for neighbor in get_neighbors(position):
            if neighbor not in region:
                yield position, neighbor


def pop_side(edges):
    edge = edges.pop()
    side = {edge}

    position, neighbor = edge
    forward = neighbor - position

    for tangent in forward.turn_left(), forward.turn_right():
        for i in count(1):
            new_position = position + i * tangent
            new_edge = new_position, new_position + forward

            if new_edge not in edges:
                break

            edges.remove(new_edge)
            side.add(new_edge)

    return side


def get_sides(region):
    edges = set(get_edges(region))

    while edges:
        yield pop_side(edges)


def solve_part_1(grid, regions):
    return sum(len(list(get_edges(region))) * len(region) for region in regions)


def solve_part_2(grid, regions):
    return sum(len(list(get_sides(region))) * len(region) for region in regions)


def main():
    grid = parse_grid(stdin)
    regions = list(get_regions(grid))

    print(solve_part_1(grid, regions))
    print(solve_part_2(grid, regions))


if __name__ == "__main__":
    main()
