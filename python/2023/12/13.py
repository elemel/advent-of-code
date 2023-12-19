from sys import stdin


def find_vertical_reflection(grid):
    # print()

    # for line in grid:
    #   print(''.join(line))

    w = len(grid[0])
    h = len(grid)

    for rx in range(1, w):
        if all(
            grid[y][rx - x - 1] == grid[y][rx + x]
            for y in range(h)
            for x in range(min(rx, w - rx))
        ):
            yield rx


def find_horizontal_reflection(grid):
    return find_vertical_reflection([*zip(*grid)])


def solve_part_1(grids):
    result = 0

    for grid in grids:
        for rx in find_vertical_reflection(grid):
            result += rx

        for ry in find_horizontal_reflection(grid):
            result += 100 * ry

    return result


def solve_part_2(grids):
    result = 0

    for grid in grids:
        seen_xs = set(find_vertical_reflection(grid))
        seen_ys = set(find_horizontal_reflection(grid))

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                grid[y][x] = ".#"[grid[y][x] == "."]

                for rx in find_vertical_reflection(grid):
                    if rx not in seen_xs:
                        seen_xs.add(rx)
                        print(x, y, "x", rx)
                        result += rx

                for ry in find_horizontal_reflection(grid):
                    if ry not in seen_ys:
                        seen_ys.add(ry)
                        print(x, y, "y", ry)
                        result += 100 * ry

                grid[y][x] = ".#"[grid[y][x] == "."]

    return result


def main():
    grids = [
        [list(line.strip()) for line in grid_str.splitlines()]
        for grid_str in stdin.read().split("\n\n")
    ]

    print(solve_part_1(grids))
    print(solve_part_2(grids))


if __name__ == "__main__":
    main()
