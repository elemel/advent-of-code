from sys import stdin
from functools import cache
from pyule import parse_grid, Vector2


def solve_part_1(grid, position, direction):
    visited_states = set()

    while True:
        state = position, direction

        if state in visited_states:
            break

        visited_states.add(state)

        position += direction

        if position not in grid:
            break

        if grid[position] == "#":
            position -= direction
            direction = direction.turn_right()

    return {position for position, direction in visited_states}


def solve_part_2(grid, position, direction, obstruction, move):
    visited_states = set()

    while True:
        state = position, direction

        if state in visited_states:
            return True

        visited_states.add(state)

        position, direction = move(position, direction, obstruction)

        if position not in grid:
            return False


def main():
    grid = parse_grid(stdin)
    [position] = [position for position, char in grid.items() if char == "^"]

    visited_positions = solve_part_1(grid, position, Vector2.UP)
    print(len(visited_positions))

    @cache
    def move(position, direction, obstruction):
        if obstruction:
            offset = obstruction - position

            if direction.cross(offset):
                return move(position, direction, None)

        position += direction

        if position not in grid:
            return position, direction

        if grid[position] == "#" or position == obstruction:
            return position - direction, direction.turn_right()

        return move(position, direction, obstruction)

    print(
        sum(
            solve_part_2(grid, position, Vector2.UP, obstruction, move)
            for obstruction in visited_positions
            if obstruction != position
        )
    )


if __name__ == "__main__":
    main()
