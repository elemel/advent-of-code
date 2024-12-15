from sys import stdin
from pyule import parse_grid, Vector2, print_grid


MOVES = {"^": Vector2.UP, "v": Vector2.DOWN, "<": Vector2.LEFT, ">": Vector2.RIGHT}


def apply_move_part_1(grid, robot, move):
    n = 0

    for i in range(1, 100):
        char = grid.get(robot + i * move)

        if char == "#":
            return robot
        elif char == ".":
            n = i
            break

    for j in range(n, 0, -1):
        grid[robot + j * move] = grid[robot + (j - 1) * move]

    grid[robot + move] = "."
    return robot + move


def can_move(grid, position, direction):
    if grid[position + direction] == "#":
        return False

    if grid[position + direction] == "[":
        return can_move(grid, position + direction, direction) and can_move(grid, position + direction + Vector2.RIGHT, direction)

    if grid[position + direction] == "]":
        return can_move(grid, position + direction, direction) and can_move(grid, position + direction + Vector2.LEFT, direction)

    assert grid[position + direction] == "."
    return True


def do_move(grid, position, direction):
    if grid[position + direction] == "[":
        do_move(grid, position + direction, direction)
        do_move(grid, position + direction + Vector2.RIGHT, direction)

    if grid[position + direction] == "]":
        do_move(grid, position + direction, direction)
        do_move(grid, position + direction + Vector2.LEFT, direction)

    grid[position + direction] = grid[position]
    grid[position] = "."


def apply_move_part_2(grid, robot, move):
    if move.x:
        return apply_move_part_1(grid, robot, move)

    if not can_move(grid, robot, move):
        return robot

    do_move(grid, robot, move)
    return robot + move


def solve_part_1(grid_str, moves):
    grid = parse_grid(grid_str.splitlines())
    [robot] = [position for position, char in grid.items() if char == "@"]
    grid[robot] = "."

    for move in moves:
        robot = apply_move_part_1(grid, robot, move)

    return sum(100 * position.y + position.x for position, char in grid.items() if char == "O")


def solve_part_2(grid_str, moves):
    grid_str = grid_str.replace("#", "##")
    grid_str = grid_str.replace("O", "[]")
    grid_str = grid_str.replace(".", "..")
    grid_str = grid_str.replace("@", "@.")

    grid = parse_grid(grid_str.splitlines())
    [robot] = [position for position, char in grid.items() if char == "@"]
    grid[robot] = "."

    # print()
    # print_grid(grid | {robot: "@"})
    # print()

    for move in moves:
        robot = apply_move_part_2(grid, robot, move)
        # print_grid(grid | {robot: "@"})
        # print()

    return sum(100 * position.y + position.x for position, char in grid.items() if char == "[")


def main():
    grid_str, moves_str = stdin.read().split("\n\n")
    moves = list(MOVES[char] for char in "".join(moves_str.split()))

    print(solve_part_1(grid_str, moves))
    print(solve_part_2(grid_str, moves))


if __name__ == "__main__":
    main()
